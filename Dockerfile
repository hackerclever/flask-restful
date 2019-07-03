FROM python:3.7-alpine

COPY . /app/

WORKDIR /app/

EXPOSE 8080

CMD [ "echo", "'hello docker'"]
