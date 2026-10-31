FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copiar código de agentes, configuración, backend y frontend
COPY 00_CONTEXT /app/00_CONTEXT
COPY 03_AGENTS /app/03_AGENTS
COPY 04_CONFIG /app/04_CONFIG
COPY 02_ENGINEERING /app/02_ENGINEERING

# Instalar dependencias Python
RUN pip install --no-cache-dir fastapi uvicorn pydantic python-dotenv httpx

EXPOSE 8088

CMD ["python", "-m", "uvicorn", "main:app", "--app-dir", "/app/02_ENGINEERING/backend", "--host", "0.0.0.0", "--port", "8088"]
