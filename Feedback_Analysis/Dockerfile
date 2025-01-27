FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Create Folder
RUN mkdir -p data output db

# Comand
CMD ["python", "main.py"]
