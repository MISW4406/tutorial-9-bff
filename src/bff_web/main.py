from fastapi import FastAPI, Request
import asyncio
from contextlib import asynccontextmanager

from pydantic_settings import BaseSettings
from typing import Any

from .consumidores import suscribirse_a_topico
from .api.v1.router import router as v1
from sse_starlette.sse import EventSourceResponse

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web AeroAlpes"}
tasks = []
eventos = list()

@asynccontextmanager
async def lifespan(app: FastAPI):
    task1 = asyncio.ensure_future(suscribirse_a_topico("eventos-reserva", "aeroalpes-bff", "public/default/eventos-reserva", eventos=eventos))
    tasks.append(task1)

    yield

    for task in tasks:
        task.cancel()

app = FastAPI(lifespan=lifespan, **app_configs)

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


app.include_router(v1, prefix="/v1")