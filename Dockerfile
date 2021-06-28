FROM python:3.6

RUN apt-get update 

RUN apt install libgl1-mesa-glx --yes

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080
CMD python api.py
