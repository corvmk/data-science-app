# Examples run as root, do not use for actual work!
FROM python:3.10-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  g++ \
  python3-dev \
  libpq-dev \
  tini \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir pip wheel && \
  pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/app
ENV PATH="/usr/app/src:$PATH"

ENTRYPOINT [ "jupyter", "lab", "--allow-root", "--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888"]
