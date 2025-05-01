from fastapi import FastAPI, Request
from celery.result import AsyncResult
from celery_worker import celery_app
from tasks import process_payment, generate_report
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def say_hello(request: Request, name=None):
    # auth_token = request.headers.get("authorization")

    # if auth_token != "Token iloveyou":
    #     return {"message": "Incorrect token"}

    return {
        "message":f"hello {name}" if name else f"hello world",
        # "message": ,
        "meta": f"love you too from the second best nikhil",
    }


@app.get("/general")
async def enqueue_general(x: int, y: int):
    task = generate_report.delay(x, y)
    return {"task_id": task.id, "status": "Processing in general queue"}


@app.get("/priority")
async def enqueue_priority(x: int, y: int):
    task = process_payment.delay(x, y)
    return {"task_id": task.id, "status": "Processing in priority queue"}


@app.get("/result/{task_id}")
async def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"status": result.status, "result": result.result}
