FROM python:3.14-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  


FROM python:3.14-slim

WORKDIR /app

RUN useradd --create-home nonRootuser

COPY --from=base /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY app/ ./app/

ENV PATH="/usr/local/bin:$PATH"

USER nonRootuser
EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]