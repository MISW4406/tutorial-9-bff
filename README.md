# Tutorial 9 - Backend for Frontends (BFFs)

Repositorio con código base para la implementación de un Backend for Frontend (BFF) usando GraphQL como lenguaje de consulta.

Este repositorio está basado en el repositorio de Sagas visto en el tutorial 8 del curso. Por tal motivo, puede usar ese mismo repositorio para entender algunos detalles que este README no cubre.

## Arquitectura

[![](https://img.plantuml.biz/plantuml/png/tLVTRjCm5BxlKrYx0eaXmGEW5SQ02wI9JU82eSgrJrElYUtvfzj0UnWUWAizGb-COpl9uZHfoyMumEg5a_F5vplV-KbwOXqrpbVbf8I58quH8ugb8rmOO4ueEPbeobQq079a3JiYFoS4LtkFWb6qr62F2BMalPeXjeRcS2qIK8lMA9M3sgjQP9QmtakkbP3Eae-Nb-S4RhK7wvGbwyrlIivAQbSlsmT0ydZSPDipKt8XYkWyRNF_S-MSgWA1dZMiT_6MDvIX86397Q6CWLM4afAIERL0EFueqZg82rn1fKkLD6iknlXisIEZpGCNXGfkgw27eKXA6mz89jp481XefmwYKodk6pRrlfEx3Bh44qfCzh3LqeAEsTQm52ow6R5xQ3YaRGkx7rEcvfgTTweg8OMA8aWe56QC2DGFAf2EyXxQObO5AgC8b0Hb5AKYIxYbXPAqp93Fg2u5mmBOFCWNX2Sl18YG2qD30ZnpM23F3nBS0l0RPLOnskPYBCejUrZJUSWvQ-lH8tN1AOTGtPN7cndysWEnIYlZg0mbIysr5muYvG76IVMyqLc9GZb83PJskngyXip66tq84TPJD7pjQa_Z3wF2Uj81qFZTDmX6SP7XKms4nck_sKR8_HyzsKIphpT7SM7z-nwrWWEZ9esLj9_fLJ7OfsFlxVJOsFpNyzVwRcI2QwFSw7YtODO2fUZOxmSA3wIbLytx9G7wu_0nhlRvAQSw598XnPVpTr79g30MHukfKuNlsri7Hghu6K2c6FWq19uKpkkZfOMtn29MMaZbqH2j7D9wlV2M6O5zPqBnmnefe6TDiJsjg7oPYhU5XmR93jf9owTHwyNV9jcBiVok1NuFRkLeC179ROlyXEAQ1Vr12hFv5G98KHgSagNVYl8hp2yKMu7R7Q76hX_MErhQ4pyBPbHJOZ7_4CJjeT0lqa4KtUqLNpvGf5a_A_Ym_nvcBvCElbCUeGJ3rzQ7quiUet2Hivel5hCRcCTKrllHl3z-PVSWUR9V7PJeZhCM_XRF25pFiB3FZCBW91-B09ydnz-MWdEGtu_VT98ITvbjIDQwleUFoDib0tKAj3iCkv21hcs-RRgm_ip9_-PqaVNJa_l92GeH_bRz0G00)](https://editor.plantuml.com/uml/tLVTRjCm5BxlKrYx0eaXmGEW5SQ02wI9JU82eSgrJrElYUtvfzj0UnWUWAizGb-COpl9uZHfoyMumEg5a_F5vplV-KbwOXqrpbVbf8I58quH8ugb8rmOO4ueEPbeobQq079a3JiYFoS4LtkFWb6qr62F2BMalPeXjeRcS2qIK8lMA9M3sgjQP9QmtakkbP3Eae-Nb-S4RhK7wvGbwyrlIivAQbSlsmT0ydZSPDipKt8XYkWyRNF_S-MSgWA1dZMiT_6MDvIX86397Q6CWLM4afAIERL0EFueqZg82rn1fKkLD6iknlXisIEZpGCNXGfkgw27eKXA6mz89jp481XefmwYKodk6pRrlfEx3Bh44qfCzh3LqeAEsTQm52ow6R5xQ3YaRGkx7rEcvfgTTweg8OMA8aWe56QC2DGFAf2EyXxQObO5AgC8b0Hb5AKYIxYbXPAqp93Fg2u5mmBOFCWNX2Sl18YG2qD30ZnpM23F3nBS0l0RPLOnskPYBCejUrZJUSWvQ-lH8tN1AOTGtPN7cndysWEnIYlZg0mbIysr5muYvG76IVMyqLc9GZb83PJskngyXip66tq84TPJD7pjQa_Z3wF2Uj81qFZTDmX6SP7XKms4nck_sKR8_HyzsKIphpT7SM7z-nwrWWEZ9esLj9_fLJ7OfsFlxVJOsFpNyzVwRcI2QwFSw7YtODO2fUZOxmSA3wIbLytx9G7wu_0nhlRvAQSw598XnPVpTr79g30MHukfKuNlsri7Hghu6K2c6FWq19uKpkkZfOMtn29MMaZbqH2j7D9wlV2M6O5zPqBnmnefe6TDiJsjg7oPYhU5XmR93jf9owTHwyNV9jcBiVok1NuFRkLeC179ROlyXEAQ1Vr12hFv5G98KHgSagNVYl8hp2yKMu7R7Q76hX_MErhQ4pyBPbHJOZ7_4CJjeT0lqa4KtUqLNpvGf5a_A_Ym_nvcBvCElbCUeGJ3rzQ7quiUet2Hivel5hCRcCTKrllHl3z-PVSWUR9V7PJeZhCM_XRF25pFiB3FZCBW91-B09ydnz-MWdEGtu_VT98ITvbjIDQwleUFoDib0tKAj3iCkv21hcs-RRgm_ip9_-PqaVNJa_l92GeH_bRz0G00)

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
