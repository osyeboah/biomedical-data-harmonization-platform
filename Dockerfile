FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --no-cache-dir --no-deps -e .

CMD ["uvicorn", "biomedical_platform.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
