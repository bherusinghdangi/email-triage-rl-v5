import os, json
from openai import OpenAI
from app.env import Task1Env, Task2Env, Task3Env
from app.models import Action

print("[START]")
envs = [Task1Env(), Task2Env(), Task3Env()]
task_ids = ["easy", "medium", "hard"]
results = []

client = OpenAI(api_key=os.environ.get("API_KEY"), base_url=os.environ.get("API_BASE_URL"))

for i, tid in enumerate(task_ids):
    env = envs[i]
    obs = env.reset()
    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Classify: {obs.subject}"}],
            max_tokens=10
        ).choices[0].message.content.lower()
    except: res = "normal"
    
    cat = "spam" if "spam" in res else "urgent" if "urgent" in res else "normal"
    _, reward, _, _ = env.step(Action(category=cat, priority=2, route="hr"))
    
    results.append({"task": tid, "score": round(float(reward), 2)})

print(json.dumps(results))
print("[END]")