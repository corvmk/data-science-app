# Examples run as root, do not use for actual work!
FROM python:3.10-bullseye

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc \
  g++ \
  python3-dev \
  libpq-dev \
  tini \
  && rm -rf /var/lib/apt/lists/*
RUN groupadd -g ${GROUP_ID} python && \
  useradd -m -r -u ${USER_ID} -g python python && \
  mkdir /usr/app && chown python:python /usr/app

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir pip wheel && \
  pip install --no-cache-dir -r requirements.txt

USER python
WORKDIR /usr/app
ENV PATH="/usr/app/src:$PATH"

ENTRYPOINT [ "jupyter", "lab", "--allow-root", "--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888"]
