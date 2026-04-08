from app.env import Task1Env, Task2Env, Task3Env
from app.grader import grade

TASKS = [
    {"id": "easy", "name": "easy", "env": Task1Env, "grader": grade},
    {"id": "medium", "name": "medium", "env": Task2Env, "grader": grade},
    {"id": "hard", "name": "hard", "env": Task3Env, "grader": grade}
]