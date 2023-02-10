from fastapi import FastAPI, Request
import asyncio
import time
import traceback
import uvicorn
import uuid

from pydantic import BaseSettings
from typing import Any

from .consumidores import suscribirse_a_topico
from .despachadores import Despachador

from . import utils

from sse_starlette.sse import EventSourceResponse

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()
eventos = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    global eventos
    task1 = asyncio.ensure_future(suscribirse_a_topico("eventos-reserva", "aeroalpes-bff", "public/default/eventos-reserva", eventos=eventos))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-revertir-pago", include_in_schema=False)
async def prueba_revertir_pago() -> dict[str, str]:
    payload = dict(
        id_usuario = "1",
        id_correlacion = "1",
        fecha_creacion = 8765432
    )
    comando = dict(
        id = str(uuid.uuid4()),
        time=utils.time_millis(),
        specversion = "v1",
        type = "ComandoReserva",
        ingestion=utils.time_millis(),
        datacontenttype="AVRO",
        service_name = "BFF-Web",
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-crear-reserva", "public/default/comando-crear-reserva")
    return {"status": "ok"}


@app.get('/stream')
async def stream_mensajes(request: Request):
    def nuevo_evento():
        global eventos
        return {'data': eventos.pop(), 'event': 'NuevoEvento'}
    async def leer_eventos():
        global eventos
        while True:
            # Si el cliente cierra la conexión deja de enviar eventos
            if await request.is_disconnected():
                break

            if len(eventos) > 0:
                yield nuevo_evento()

            await asyncio.sleep(0.1)

    return EventSourceResponse(leer_eventos())