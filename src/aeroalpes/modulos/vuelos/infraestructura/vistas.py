from aeroalpes.seedwork.infraestructura.vistas import Vista
from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.config.db import db
from .dto import Reserva as ReservaDTO

class VistaReserva(Vista):
    def obtener_todos(self):
        reservas_dto = db.session.query(ReservaDTO).all()
        reservas = list()

        for reserva_dto in reservas_dto:
            reservas.append(Reserva(id=reserva_dto.id, 
                fecha_creacion=reserva_dto.fecha_creacion, 
                fecha_actualizacion=reserva_dto.fecha_actualizacion))
        
        return reservas

    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs) -> [Reserva]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if estado:
            params['estado'] = str(estado)
        
        if id_cliente:
            params['id_cliente'] = str(id_cliente)
            
        # TODO Convierta ReservaDTO a Reserva y valide que la consulta es correcta
        return db.session.query(ReservaDTO).filter_by(**params)
