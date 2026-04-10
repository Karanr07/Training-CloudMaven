FROM python:3.12-slim

WORKDIR /app
COPY log_generator.py .

# No external deps – pure stdlib
CMD ["python", "-u", "log_generator.py"]
