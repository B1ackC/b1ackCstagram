FROM python:3.12.1-slim

WORKDIR /app

COPY requirements.txt /app
COPY my_falsk_project /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENV FLASK_APP=app.py

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0", "--port=8080"]