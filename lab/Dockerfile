# syntax=docker/dockerfile:1

# Nella settimana 05 riscrivi questo file da zero senza guardarlo, poi confronta:
# la differenza è esattamente quello che ti manca su Docker.

# --- Stage 1: costruisce la wheel ---
FROM python:3.12-slim AS build
WORKDIR /src
COPY pyproject.toml ./
COPY src ./src
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels .

# --- Stage 2: runtime ---
FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    RAG_ENVIRONMENT=container
RUN useradd --create-home --uid 10001 app
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir /wheels/*.whl && rm -rf /wheels
USER app
ENTRYPOINT ["python", "-m", "rag"]
