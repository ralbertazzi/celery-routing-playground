from celery import Celery
import celeryconfig
from route import route_task


celery_app = Celery("playground")
celery_app.config_from_object(celeryconfig)
celery_app.conf.task_routes = [route_task]
