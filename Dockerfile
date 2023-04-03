FROM python:3.12.0a6-bullseye
WORKDIR /app

# Install the Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Source code of Fossil.
COPY ./src ./src

# Entrypoint into our app.
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD python src/main.py
