FROM python:3.10-bullseye

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir pip wheel && \
    pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/app

ENTRYPOINT [ "jupyter", "lab", "--allow-root", "--ServerApp.ip=0.0.0.0", "--ServerApp.port=8888" ]