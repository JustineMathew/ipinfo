FROM python:3.6-alpine3.8


ENV ACCESS_KEY= 

WORKDIR /usr/src/app

COPY ipinfo.py ./

COPY requirements.txt  ./

RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3","./ipinfo.py"]
