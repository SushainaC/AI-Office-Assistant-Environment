import os
import requests
from env.environment import OfficeEnv
from env.models import Action

# Hugging Face API setup
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# Initialize environment
env = OfficeEnv()
obs = env.reset()

total_reward = 0

for _ in range(5):
    prompt = f"""
    You are an AI assistant.

    Task: {obs.task_type}
    Content: {obs.content}

    What is the best action to take?
    """

    try:
        result = query({"inputs": prompt})

        # Extract response safely
        if isinstance(result, list) and "generated_text" in result[0]:
            action_text = result[0]["generated_text"]
        else:
            action_text = str(result)

    except Exception as e:
        print("API Error:", e)
        action_text = "take appropriate action"

    action = Action(
        action_type="text",
        content=action_text
    )

    obs, reward, done, info = env.step(action)
    total_reward += reward

    print(f"Step Reward: {reward}")

    if done:
        break

print("Final Score:", total_reward)