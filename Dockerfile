FROM python:latest

RUN apt-get update && apt-get install -y --no-install-recommends whois

COPY . /cct

WORKDIR /cct

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
