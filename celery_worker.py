from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=['tasks']
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_routes={
        "tasks.priproty_task": {"queue": "prioroty"},
        "tasks.general_task": {"queue": "general"},
    },
    task_queue_max_priority=10,
    task_default_priority=5,
)
