FROM python:3.12.1-slim

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]