from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from typing import Optional
from starlette.requests import Request
import json

with open('redis_config.json') as f:
    redis_config = json.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_db = get_redis_connection(
    host = redis_config['host'].split(':')[0],
    port = redis_config['host'].split(':')[1],
    password = redis_config['password'],
    decode_responses = True
)

class Task(HashModel):
    name: str
    complete: Optional[bool] = 0

    class Meta:
        db = redis_db

@app.get("/tasks")
async def all():
    return [format(pk) for pk in Task.all_pks()]

def format(pk: str):
    task = Task.get(pk)

    return {
        'id': task.pk,
        'name': task.name,
        'complete': task.complete
    }

@app.post('/tasks')
async def create(task: Task):
    return task.save()

@app.put('/tasks/{pk}')
async def update(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.complete = int(body['complete'])

    return task.save()

@app.delete('/tasks/{pk}')
async def delete(pk: str):
    task = Task.get(pk)

    return task.delete(pk)