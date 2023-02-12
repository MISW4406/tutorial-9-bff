from dataclasses import dataclass
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.vuelos.dominio.entidades import Reserva
from aeroalpes.modulos.vuelos.aplicacion.dto import ReservaDTO
from .base import ReservaQueryBaseHandler

@dataclass
class ObtenerTodasReservas(Query):
    ...

class ObtenerTodasReservasHandler(ReservaQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        reservas_dto = []
        vista = self.fabrica_vista.crear_objeto(Reserva)
        reservas = vista.obtener_todos()

        for reserva in reservas:
            dto = ReservaDTO(
                fecha_creacion=reserva.fecha_creacion.strftime(self.FORMATO_FECHA),
                fecha_actualizacion=reserva.fecha_actualizacion.strftime(self.FORMATO_FECHA),
                id = reserva.id
            )
            reservas_dto.append(dto)
        
        return QueryResultado(resultado=reservas_dto)

@query.register(ObtenerTodasReservas)
def ejecutar_query_obtener_reserva(query: ObtenerTodasReservas):
    handler = ObtenerTodasReservasHandler()
    return handler.handle(query)