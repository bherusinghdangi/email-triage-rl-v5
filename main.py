import os
from fastapi import FastAPI, Request
from app.env import Task1Env, Task2Env, Task3Env
from app.models import Action
from typing import Dict

app = FastAPI()

# Registry of tasks
tasks = {"easy": Task1Env(), "medium": Task2Env(), "hard": Task3Env()}
current_env = tasks["easy"]

@app.get("/")
def home():
    return {"status": "online", "active_tasks": list(tasks.keys())}

@app.post("/reset")
async def reset(request: Request, task_id: str = None):
    global current_env
    # Check URL params first, then JSON body
    tid = task_id
    if not tid:
        try:
            body = await request.json()
            tid = body.get("task_id")
        except:
            tid = "easy"
    
    current_env = tasks.get(tid if tid in tasks else "easy")
    return current_env.reset().dict()

@app.post("/step")
def step(action: Dict):
    try:
        # Force strict 0.8/0.2 rewards
        obs, reward, done, info = current_env.step(Action(**action))
        return {
            "observation": obs.dict(),
            "reward": float(max(0.2, min(0.8, float(reward)))), 
            "done": bool(done),
            "info": info
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/state")
def state():
    return current_env.state().dict()