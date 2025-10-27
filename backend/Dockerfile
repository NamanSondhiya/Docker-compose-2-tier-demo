FROM python:3.14.0b3-alpine3.21

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /app

ENTRYPOINT [ "python" ]

CMD [ "arpi.py" ]
    
