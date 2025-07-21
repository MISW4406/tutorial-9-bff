# Tutorial 9 - Backend for Frontends (BFFs)

Repositorio con código base para la implementación de un Backend for Frontend (BFF) usando GraphQL como lenguaje de consulta.

Este repositorio está basado en el repositorio de Sagas visto en el tutorial 8 del curso. Por tal motivo, puede usar ese mismo repositorio para entender algunos detalles que este README no cubre.

## Arquitectura

[![](https://img.plantuml.biz/plantuml/png/tLTDRXCn5Dxd55PN854aE01gQ2cmGAfe9HO8HOxzCd4pOxl-2IseX-40h7g4N8ndUsOwdimaOL4MM97YyVlizxtVyPnOHutpLJafOU68KyI8Oka85mQO4qfE9fgo5Is075d3ZiZF2S7Hhb4mYfOQx16XbhHFCyJMq1okHG9gqGgbSb1hLOjC4iOxoRKIqbdouUhgWi2jzc2TicIz-Kt9UKdjwcMx0IIFnqssDJCb5wA8ojCqrpzNpgag4EX9mpYDIzvGXWu1I-u8PGoi8fIKbCof1SBnHv7MGLpW6YfTgkIpvc6CpvOyCjeyS56eeBOA_Z0KIMdZ0Sc4HJI2WNRg83gLuhvXKyyxiSkWIpoXn60FIoqjw9Xi3Kl1efeHkOU6GvgsiFinpzHSi_FEL2MaKD494Wg54IC2_GSLI4Tv3sqngW8zemYK1DqeIaMMS4iB9McP8PzHNGg62R1va2y8Jre8424NXeO0UEOmGPuVv70BmByhiuhMDWzZLcx9mvZEGynPcuyUgGjEEOJihZmkPl0R3yGghOoZCgGiDJTUE8YK1nWdh-U5pafqb8DKG6c-gy1ho6oyq8SGOJn5mTUgzXJ-C2gC9sq0ZTvzZM0K5na-LKDejFQBROJS_r6JZJNxQdCK5yQ_hr4hE31gKbj9yvbU5ODrElRUJjl6-h-UlzPt8nrS6-L6sxi5inReYexyVY3nG5fwtRnV4g3V3X_jQlTFETKXaGmfFb-SHaz63sDoj9WwLFY-lNLWf8hN0395mwV1yEJXF3zQMhWa5Z7JGYYFXcZba5RhfRVC2Amx4v8VraW1DMkAvMb5vSkKl2qy54Xsq4vQFhLQB_uso5wCnNSjy3wu5QF1G2IrBV8ZEjSiw0zIcCslO42oqc2NBFsMbLzWVgdO2jnk2pLM_R2_ewGzyPDWHZKf5kCFmRaz5Ef5EeYYkxNYomUArEjd1H_MtyFiPTB1Tz8Zf62uRRq_k-mn2Wyvg_bY4SE8_wFnVhnTzo1va5yT5E1QKGjzY_i3ltDCvdEZq239nrZZNdByTIau1_dj-4qd476MoOPSMUVqy15vYMIWJb9s6s0NCb2fpNsc2-ltcVpJfekiTq_k9oVeYF0fzGS0)](https://editor.plantuml.com/uml/tLTDRXCn5Dxd55PN854aE01gQ2cmGAfe9HO8HOxzCd4pOxl-2IseX-40h7g4N8ndUsOwdimaOL4MM97YyVlizxtVyPnOHutpLJafOU68KyI8Oka85mQO4qfE9fgo5Is075d3ZiZF2S7Hhb4mYfOQx16XbhHFCyJMq1okHG9gqGgbSb1hLOjC4iOxoRKIqbdouUhgWi2jzc2TicIz-Kt9UKdjwcMx0IIFnqssDJCb5wA8ojCqrpzNpgag4EX9mpYDIzvGXWu1I-u8PGoi8fIKbCof1SBnHv7MGLpW6YfTgkIpvc6CpvOyCjeyS56eeBOA_Z0KIMdZ0Sc4HJI2WNRg83gLuhvXKyyxiSkWIpoXn60FIoqjw9Xi3Kl1efeHkOU6GvgsiFinpzHSi_FEL2MaKD494Wg54IC2_GSLI4Tv3sqngW8zemYK1DqeIaMMS4iB9McP8PzHNGg62R1va2y8Jre8424NXeO0UEOmGPuVv70BmByhiuhMDWzZLcx9mvZEGynPcuyUgGjEEOJihZmkPl0R3yGghOoZCgGiDJTUE8YK1nWdh-U5pafqb8DKG6c-gy1ho6oyq8SGOJn5mTUgzXJ-C2gC9sq0ZTvzZM0K5na-LKDejFQBROJS_r6JZJNxQdCK5yQ_hr4hE31gKbj9yvbU5ODrElRUJjl6-h-UlzPt8nrS6-L6sxi5inReYexyVY3nG5fwtRnV4g3V3X_jQlTFETKXaGmfFb-SHaz63sDoj9WwLFY-lNLWf8hN0395mwV1yEJXF3zQMhWa5Z7JGYYFXcZba5RhfRVC2Amx4v8VraW1DMkAvMb5vSkKl2qy54Xsq4vQFhLQB_uso5wCnNSjy3wu5QF1G2IrBV8ZEjSiw0zIcCslO42oqc2NBFsMbLzWVgdO2jnk2pLM_R2_ewGzyPDWHZKf5kCFmRaz5Ef5EeYYkxNYomUArEjd1H_MtyFiPTB1Tz8Zf62uRRq_k-mn2Wyvg_bY4SE8_wFnVhnTzo1va5yT5E1QKGjzY_i3ltDCvdEZq239nrZZNdByTIau1_dj-4qd476MoOPSMUVqy15vYMIWJb9s6s0NCb2fpNsc2-ltcVpJfekiTq_k9oVeYF0fzGS0)

## Estructura del proyecto

Este repositorio sigue en general la misma estructura del repositorio de origen. Sin embargo, cuenta con unos ligeros cambios en especial en la estructura del módulo `ui` y el nuevo servicio `bff`:

- El directorio **src/bff_web/** incluye el código del BFF Web. Este servicio cuenta con la siguiente estructura:
    - **consumidores**: Código con la lógica para leer y procesar eventos del broker de eventos.
    - **despachadores**: Código con la lógica para publicar comandos al broker de eventos.
    - **main**: Archivo con la lógica de despliegue y configuración del servidor.
    - **api**: Módulo con la diferentes versiones del API, routers, esquemas, mutaciones y consultas.
- El directorio **src/ui/** cuenta ahora solo con código HTML, estilos CSS y JS. 

## AeroAlpes
### Ejecutar Base de datos
Desde el directorio principal ejecute el siguiente comando.

```bash
docker-compose --profiles db up
```

Este comando descarga las imágenes e instala las dependencias de la base datos.

### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/aeroalpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/aeroalpes/api --debug run
```

### Ejecutar pruebas

```bash
coverage run -m pytest
```

### Ver reporte de covertura
```bash
coverage report
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f aeroalpes.Dockerfile -t aeroalpes/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 aeroalpes/flask
```

## Sidecar/Adaptador
### Instalar librerías

En el mundo real es probable que ambos proyectos estén en repositorios separados, pero por motivos pedagógicos y de simpleza, 
estamos dejando ambos proyectos en un mismo repositorio. Sin embargo, usted puede encontrar un archivo `sidecar-requirements.txt`, 
el cual puede usar para instalar las dependencias de Python para el servidor y cliente gRPC.

```bash
pip install -r sidecar-requirements.txt
```

### Ejecutar Servidor

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/main.py 
```

### Ejecutar Cliente

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/cliente.py 
```

### Compilación gRPC

Desde el directorio `src/sidecar` ejecute el siguiente comando.

```bash
python -m grpc_tools.protoc -Iprotos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py protos/vuelos.proto
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f adaptador.Dockerfile -t aeroalpes/adaptador
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 50051:50051 aeroalpes/adaptador
```

## Microservicio Notificaciones
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/notificaciones/main.py
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f notificacion.Dockerfile -t aeroalpes/notificacion
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run aeroalpes/notificacion
```

## Microservicio: Clientes

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn cliente.main:app --host localhost --port 8000 --reload
```

## Microservicio: Pagos

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn pagos.main:app --host localhost --port 8001 --reload
```

## Microservicio: Integración GDS

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn integracion_gds.main:app --host localhost --port 8002 --reload
```

## BFF: Web

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn bff_web.main:app --host localhost --port 8003 --reload
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f ui.Dockerfile -t aeroalpes/bff
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run aeroalpes/bff
```

## CDC & Debezium

**Nota**: Antes de poder ejectuar todos los siguientes comandos DEBE tener la base de datos MySQL corriendo.

### Descargar conector de Debezium

```
wget https://archive.apache.org/dist/pulsar/pulsar-2.10.1/connectors/pulsar-io-debezium-mysql-2.10.1.nar
```

### Ejecutar Debezium
Abrir en una terminal:

```bash
docker exec -it broker bash
```

Ya dentro de la contenedora ejecute:
```bash
./bin/pulsar-admin source localrun --source-config-file /pulsar/connectors/debezium-mysql-source-config.yaml --destination-topic-name debezium-mysql-topic
```

### Consumir eventos Debezium

Abrir en una terminal:

```bash
docker exec -it broker bash
```

Ya dentro de la contenedora ejecute:

```bash
./bin/pulsar-client consume -s "sub-datos" public/default/aeroalpesdb.reservas.usuarios_legado -n 0
```

### Consultar tópicos
Abrir en una terminal:

```bash
docker exec -it broker bash
```

Ya dentro de la contenedora ejecute:

```bash
./bin/pulsar-admin topics list public/default
```

### Cambiar retención de tópicos
Abrir en una terminal:

```bash
docker exec -it broker bash
```
Ya dentro de la contenedora ejecute:

```bash
./bin/pulsar-admin namespaces set-retention public/default --size -1 --time -1
```

Para poder ver que los cambios fueron efectivos ejecute el siguiente comando:

```bash
./bin/pulsar-admin namespaces get-retention public/default
```

**Nota**: Esto nos dejará con una retención infinita. Sin embargo, usted puede cambiar la propiedad de `size` para poder usar [Tiered Storage](https://pulsar.apache.org/docs/2.11.x/concepts-tiered-storage/)

### Instrucciones oficiales

Para seguir la guía oficial de instalación y uso de Debezium en Apache Pulsar puede usar el siguiente [link](https://pulsar.apache.org/docs/2.10.x/io-cdc-debezium/)


## Docker-compose

Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```

En caso de querer desplegar dicha topología en el background puede usar el parametro `-d`.

```bash
docker-compose up -d
```

## Comandos útiles

### Listar contenedoras en ejecución
```bash
docker ps
```

### Listar todas las contenedoras
```bash
docker ps -a
```

### Parar contenedora
```bash
docker stop <id_contenedora>
```

### Eliminar contenedora
```bash
docker rm <id_contenedora>
```

### Listar imágenes
```bash
docker images
```

### Eliminar imágenes
```bash
docker images rm <id_imagen>
```

### Acceder a una contendora
```bash
docker exec -it <id_contenedora> sh
```

### Kill proceso que esta usando un puerto
```bash
fuser -k <puerto>/tcp
```

### Correr docker-compose usando profiles
```bash
docker-compose --profile <pulsar|aeroalpes|ui|notificacion> up
```
