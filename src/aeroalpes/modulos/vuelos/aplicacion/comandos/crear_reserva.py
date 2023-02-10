from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.vuelos.aplicacion.dto import ItinerarioDTO, ReservaDTO
from .base import CrearReservaBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioReservas, RepositorioEventosReservas

from pydispatch import dispatcher

@dataclass
class CrearReserva(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    itinerarios: list[ItinerarioDTO]


class CrearReservaHandler(CrearReservaBaseHandler):
    
    def handle(self, comando: CrearReserva):
        reserva_dto = ReservaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        reserva.crear_reserva(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioReservas)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosReservas)

        from aeroalpes.config.db import db

        # TODO Debido al uso de multi-thread el uso de sesiones Flask no es permitido. ¿Como cree que podría implementarse
        # una UnidadDeTrabajo en este caso?
        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva, repositorio_eventos_func=repositorio_eventos.agregar)
        #UnidadTrabajoPuerto.commit()
        repositorio.agregar(reserva)

        for evento in reserva.eventos:
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
            
        db.session.commit()


@comando.register(CrearReserva)
def ejecutar_comando_crear_reserva(comando: CrearReserva):
    handler = CrearReservaHandler()
    handler.handle(comando)
    