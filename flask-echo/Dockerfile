FROM python:3.8

WORKDIR app/

RUN pip3 install requests flask

COPY app/ .

CMD [ "python3", "-m" , "flask", "run" ,"-h", "::0" ]
