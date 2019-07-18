FROM python:3.7-alpine

COPY . /app/

WORKDIR /app/

RUN pip install --upgrade pip
RUN pip install flask flask_restplus waitress

EXPOSE 8080

CMD [ "python", "src/app.py"]
