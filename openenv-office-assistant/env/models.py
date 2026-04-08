from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    inbox: List[str]
    task: str

class Action(BaseModel):
    action_type: str
    content: str

class Reward(BaseModel):
    score: float
    feedback: str