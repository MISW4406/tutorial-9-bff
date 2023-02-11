import typing
import strawberry
import datetime
import uuid

from bff_web import utils
from bff_web.despachadores import Despachador

def obtener_reservas(root) -> typing.List["Reserva"]:
    return [Reserva(id="12", id_usuario="12121", fecha_creacion=datetime.datetime.now())]

def obtener_reserva_por_id(root) -> "Reserva":
    return Reserva(id="12", id_usuario="12121", fecha_creacion=datetime.datetime.now())

def obtener_reserva_por_id_usuario(root) -> "Reserva":
    return Reserva(id="12", id_usuario="12121", fecha_creacion=datetime.datetime.now())


@strawberry.type
class Reserva:
    id: str = strawberry.field(resolver=obtener_reserva_por_id)
    id_usuario: str = strawberry.field(resolver=obtener_reserva_por_id_usuario)
    fecha_creacion: datetime.datetime

@strawberry.type
class ReservaRespuesta:
    mensaje: str
    codigo: int

@strawberry.type
class Query:
    reservas: typing.List[Reserva] = strawberry.field(resolver=obtener_reservas)


@strawberry.type
class Mutation:

    # TODO Crear un objeto strawberry para incluir los itinerarios
    @strawberry.mutation
    async def crear_reserva(self, id_usuario: str, id_correlacion: str) -> ReservaRespuesta:
        print(f"ID Usuario: {id_usuario}, ID Correlación: {id_correlacion}")
        payload = dict(
            id_usuario = id_usuario,
            id_correlacion = id_correlacion,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        despachador.publicar_mensaje(comando, "comando-crear-reserva", "public/default/comando-crear-reserva")
        return ReservaRespuesta(mensaje="Procesando Mensaje", codigo=203)


schema = strawberry.Schema(query=Query, mutation=Mutation)