from .models import Observation, Action, Reward
import random

class OfficeEnv:

    def __init__(self):
        self.state_data = {}
        self.current_task = None
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        self.current_task = random.choice(["email", "schedule", "support"])

        self.state_data = {
            "inbox": [
                "Meeting request from manager",
                "Spam email: win lottery",
                "Client complaint about delay"
            ]
        }

        return Observation(
            inbox=self.state_data["inbox"],
            task=self.current_task
        )

    def step(self, action: Action):
        self.step_count += 1

        reward = 0.0
        done = False
        feedback = ""

        # simple logic
        if self.current_task == "email":
            if "spam" in action.content.lower():
                reward += 0.5
                feedback = "Correctly identified spam"
        
        if self.step_count > 3:
            done = True

        return (
            Observation(
                inbox=self.state_data["inbox"],
                task=self.current_task
            ),
            reward,
            done,
            {"feedback": feedback}
        )

    def state(self):
        return self.state_data