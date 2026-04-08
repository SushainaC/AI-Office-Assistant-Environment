import os
from openai import OpenAI
from env.environment import OfficeEnv
from env.models import Action

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

env = OfficeEnv()
obs = env.reset()

total_reward = 0

for _ in range(5):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": str(obs)}]
    )

    action_text = response.choices[0].message.content

    action = Action(
        action_type="text",
        content=action_text
    )

    obs, reward, done, info = env.step(action)
    total_reward += reward

    if done:
        break

print("Final Score:", total_reward)