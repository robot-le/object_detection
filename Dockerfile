FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/
ADD .env.docker /code/.env

RUN apt-get update -y && apt-get install libglib2.0-0 libsm6 libxrender1 libxext6 libgl1 -y
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000