FROM ubuntu:20.04

COPY . /usr/app/

EXPOSE 5000
 
WORKDIR /usr/app/

#RUN pip install -r requirements.txt
RUN set -xe \
    && apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip

# RUN pip install --upgrade pip
# apt-get -yqq install python3-pip
RUN pip install -r ./requirements.txt

CMD python3 flask_app.py

