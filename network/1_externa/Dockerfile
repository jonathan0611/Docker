FROM python:3.8


WORKDIR /app

COPY . .

RUN apt-get install python-dev default-libmysqlclient-dev libssl-dev -Y
RUN pip install pip --upgrade
RUN pip install mysql-connector-python  Flask requests

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD   ["./app.py"]
