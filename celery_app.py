from celery import Celery

celery_app = Celery()
# celery_app.conf.broker_url = "redis://localhost"
# Задача запускается в вызывающем потоке!
celery_app.conf.task_always_eager = True
