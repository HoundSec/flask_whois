FROM python:latest

COPY . /cct

WORKDIR /cct

RUN pip install -r requirements.txt

CMD ["gunicorn","-b","0.0.0.0:8000","app:app"]

EXPOSE 8000
