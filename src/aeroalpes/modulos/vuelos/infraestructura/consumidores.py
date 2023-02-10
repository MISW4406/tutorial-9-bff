import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from aeroalpes.modulos.vuelos.infraestructura.schema.v1.eventos import EventoReservaCreada
from aeroalpes.modulos.vuelos.infraestructura.schema.v1.comandos import ComandoCrearReserva

from aeroalpes.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando

from aeroalpes.modulos.vuelos.infraestructura.proyecciones import ProyeccionReservasLista, ProyeccionReservasTotales
from aeroalpes.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from aeroalpes.seedwork.infraestructura import utils
from aeroalpes.modulos.vuelos.aplicacion.dto import ItinerarioDTO

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-reserva', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoReservaCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')

            # TODO Identificar el tipo de CRUD del evento: Creacion, actualización o eliminación.
            ejecutar_proyeccion(ProyeccionReservasTotales(datos.fecha_creacion, ProyeccionReservasTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionReservasLista(datos.id_reserva, datos.id_cliente, datos.estado, datos.fecha_creacion, datos.fecha_creacion), app=app)
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-crear-reserva', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-crear-reserva', schema=AvroSchema(ComandoCrearReserva))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()

            print(f'Comando recibido: {mensaje.value()}')

            fecha_creacion = utils.millis_a_datetime(valor.data.fecha_creacion).strftime('%Y-%m-%dT%H:%M:%SZ')
            id_reserva = str(uuid.uuid4())
            itinerarios = [ItinerarioDTO(odos=[])]
            # TODO Debe poderse crear los itinerarios

            try:
                with app.app_context():
                    comando = CrearReserva(fecha_creacion, fecha_creacion, id_reserva, itinerarios)
                    ejecutar_commando(comando)
            except:
                logging.error('ERROR: Procesando eventos!')
                traceback.print_exc()

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()