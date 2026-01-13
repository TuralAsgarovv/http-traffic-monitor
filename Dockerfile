# Multi-stage build istifadə edirik (optimal ölçü üçün)
FROM python:3.9-slim as builder

WORKDIR /app

# Sistem asılılıqları (scapy üçün libpcap lazımdır)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final image
FROM python:3.9-slim

WORKDIR /app

# Libpcap-i runtime image-ə də əlavə etməliyik
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpcap0.8 \
    && rm -rf /var/lib/apt/lists/*

# Builder-dən quraşdırılmış paketləri kopyalayırıq
COPY --from=builder /root/.local /root/.local

# Kodu kopyalayırıq
COPY . .

# PATH-i yeniləyirik
ENV PATH=/root/.local/bin:$PATH

# Log qovluğunu yaradırıq
RUN mkdir -p logs

# Default əmr
CMD ["python3", "src/main.py"]