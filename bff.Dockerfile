FROM python:3.12

EXPOSE 8003/tcp

COPY bff-requirements.txt ./
RUN pip install --no-cache-dir -r bff-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "bff_web.main:app", "--host", "localhost", "--port", "8003", "--reload"]