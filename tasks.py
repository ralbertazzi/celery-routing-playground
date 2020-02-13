from time import sleep

from celeryapp import celery_app


@celery_app.task
def io_bounded():
    sleep(5)


@celery_app.task
def io_bounded_hp():
    sleep(5)


@celery_app.task
def cpu_bounded():
    sleep(5)
