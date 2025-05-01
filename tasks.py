import time

from celery_worker import celery_app


@celery_app.task(queue="priority")
def process_payment(x: int, y: int) -> int:
    print("pri")
    time.sleep(20)
    return x * y

@celery_app.task(queue="general")
def generate_report(x: int, y: int) -> int:
    print("gen")
    # time.sleep(15)
    return x + y
