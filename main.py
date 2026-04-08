from openenv.server.app import create_app
from app.env import Task1Env, Task2Env, Task3Env

# This single line automatically builds all the FastAPI routes AND tells the grader you have 3 tasks
app = create_app([Task1Env, Task2Env, Task3Env])

def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()