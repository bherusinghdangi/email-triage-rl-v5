import os
from fastapi import FastAPI, Request
from app.env import Task1Env, Task2Env, Task3Env
from app.models import Action
from typing import Dict

app = FastAPI()

task_map = {"easy": Task1Env(), "medium": Task2Env(), "hard": Task3Env()}
current_env = task_map["easy"]

@app.get("/")
def home(): return {"status": "online", "tasks": list(task_map.keys())}

@app.post("/reset")
async def reset(request: Request):
    global current_env
    try:
        body = await request.json()
        tid = body.get("task_id", "easy")
    except: tid = "easy"
    current_env = task_map.get(tid, task_map["easy"])
    return current_env.reset().dict()

@app.post("/step")
def step(action: Dict):
    try:
        obs, reward, done, info = current_env.step(Action(**action))
        return {"observation": obs.dict(), "reward": float(reward), "done": bool(done), "info": info}
    except Exception as e: return {"error": str(e)}

@app.get("/state")
def state(): return current_env.state().dict()