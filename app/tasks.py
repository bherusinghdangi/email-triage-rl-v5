from app.env import Task1Env, Task2Env, Task3Env
from app.grader import SafeGrader, grade

grader_instance = SafeGrader()

# We attach the 'env' and 'grader' directly to the task definition. 
# When the validator imports this, it physically sees 3 fully equipped tasks.
TASKS = [
    {
        "id": "easy",
        "name": "easy",
        "env": Task1Env,
        "grader": grader_instance
    },
    {
        "id": "medium",
        "name": "medium",
        "env": Task2Env,
        "grader": grader_instance
    },
    {
        "id": "hard",
        "name": "hard",
        "env": Task3Env,
        "grader": grader_instance
    }
]

# We also provide a dictionary format just in case the validator parses by key.
TASK_REGISTRY = {
    "easy": TASKS[0],
    "medium": TASKS[1],
    "hard": TASKS[2]
}