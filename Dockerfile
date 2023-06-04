FROM python:3.10
ENV PYTHONUNBUFFERED 1

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh