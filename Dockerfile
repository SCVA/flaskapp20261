# Instalar python para flask
FROM python:3.14.4-alpine3.23
WORKDIR /usr/src/app

# Instalar requerimientos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar la aplicación
COPY . .
ENV FLASK_ENV=production
EXPOSE 80
CMD [ "python", "./app.py" ]
