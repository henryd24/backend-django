FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requeriments /app/requeriments.txt
RUN apt-get install default-libmysqlclient-dev
RUN pip install -r requeriments.txt
COPY . /app