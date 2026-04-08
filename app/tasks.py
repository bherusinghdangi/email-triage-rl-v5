from app.env import Task1Env, Task2Env, Task3Env

def programmatic_grader(reward, *args, **kwargs):
    # Mathematically locked between 0.1 and 0.9
    return float(max(0.15, min(0.85, float(reward))))

TASKS = [
    {"id": "easy", "name": "easy", "env": Task1Env, "grader": programmatic_grader},
    {"id": "medium", "name": "medium", "env": Task2Env, "grader": programmatic_grader},
    {"id": "hard", "name": "hard", "env": Task3Env, "grader": programmatic_grader}
]