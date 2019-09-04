FROM python:alpine3.9

ENV TZ=Asia/Phnom_Penh


RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk --no-cache add tzdata openntpd && \
    apk --no-cache add  postgresql-dev gcc python-dev musl-dev && \
    mkdir app

WORKDIR app

RUN mkdir ndscheduler simple_scheduler

COPY ./ndscheduler /app/ndscheduler

RUN touch /app/ndscheduler/__init__.py

COPY ./simple_scheduler /app/simple_scheduler

COPY ./.docker .

RUN pip install -r /app/simple_scheduler/requirements.txt

ENTRYPOINT ["python", "./scheduler.py"]