import random
from app.models import Observation

# Isolated data for each task
DATA_EASY = [{"text": "Buy now!", "sender": "ads@spam.com", "subject": "SALE", "cat": "spam"}]
DATA_MED = [{"text": "Server down", "sender": "admin@co.com", "subject": "URGENT", "cat": "urgent"}]
DATA_HARD = [{"text": "HR Meeting", "sender": "hr@co.com", "subject": "Meeting", "cat": "normal"}]

class Task1Env:
    def __init__(self): self.current = None
    def reset(self):
        self.current = random.choice(DATA_EASY)
        return self.state()
    def state(self):
        return Observation(email_text=self.current["text"], sender=self.current["sender"], subject=self.current["subject"])
    def step(self, action):
        ans = getattr(action, 'category', str(action)).lower().strip()
        reward = 0.8 if ans == self.current["cat"] else 0.2
        return self.state(), reward, True, {}

class Task2Env:
    def __init__(self): self.current = None
    def reset(self):
        self.current = random.choice(DATA_MED)
        return self.state()
    def state(self):
        return Observation(email_text=self.current["text"], sender=self.current["sender"], subject=self.current["subject"])
    def step(self, action):
        ans = getattr(action, 'category', str(action)).lower().strip()
        reward = 0.8 if ans == self.current["cat"] else 0.2
        return self.state(), reward, True, {}

class Task3Env:
    def __init__(self): self.current = None
    def reset(self):
        self.current = random.choice(DATA_HARD)
        return self.state()
    def state(self):
        return Observation(email_text=self.current["text"], sender=self.current["sender"], subject=self.current["subject"])
    def step(self, action):
        ans = getattr(action, 'category', str(action)).lower().strip()
        reward = 0.8 if ans == self.current["cat"] else 0.2
        return self.state(), int(reward), True, {}