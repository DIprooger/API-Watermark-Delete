######################## STAGE 1: build wheels ########################
FROM python:3.11-slim AS builder

# Системные зависимости для Torch и OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential git libgl1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements-runtime.txt .

# Собираем все пакеты в колёсики — ускоряет финальный install
RUN pip install --upgrade pip wheel && \
    pip wheel -r requirements-runtime.txt -w /wheels

######################## STAGE 2: runtime #############################
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1

# ── устанавливаем готовые колёсики ───────────────────────────────────
COPY --from=builder /wheels /wheels
RUN pip install --no-index --find-links=/wheels /wheels/*

# ── добавляем код и веса ────────────────────────────────────────────
WORKDIR /app
COPY . /app


# ── переменные окружения из .env (подхватываются python-dotenv) ─────
COPY .env /app/.env

EXPOSE 8886
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8886", "--workers", "4"]
