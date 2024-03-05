FROM ubuntu:20.04

COPY . /usr/app/

EXPOSE 5000
 
WORKDIR /usr/app/

RUN apt-get update \
    && apt-get install -y python3 \ 
    && pip install -r requirements.txt

CMD python flask_app.py

