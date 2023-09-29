import os
import openai
import json
import time

# Set your API key as an environment variable or load it from a file
os.environ["OPENAI_API_KEY"] = "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"

# Authenticate with OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=256
    )
    return response.choices[0].message['content']

def get_preference(aspects, pref_type):
    prefs = aspects[pref_type]
    print(f"Choose a {pref_type}:")
    for i, pref in enumerate(prefs, 1):
        print(f"{i}. {pref['name']}")
    choice = int(input("Enter the number corresponding to your choice: "))
    return prefs[choice - 1]['description']

def generate_super_prompt(aspects):
    topics = get_preference(aspects, "topics")
    conditions = get_preference(aspects, "conditions")
    flow = get_preference(aspects, "conversation_flow")
    background = get_preference(aspects, "backgrounds")
    evidence = get_preference(aspects, "evidence")
    behaviors = get_preference(aspects, "behaviors")
    incidents = get_preference(aspects, "incidents")
    actors = get_preference(aspects, "actors")
    threats = get_preference(aspects, "threats")
    victim = get_preference(aspects, "victim")

    super_prompt = f"You are {actors} who used a {threats} against {victim}. {background} {incidents} {behaviors} {evidence} {flow} {conditions}. do not mention the fact that this is a training scenario. if the victim tries to go off topic, make sure to get back on topic. \nAttacker: "
    return super_prompt

# Load aspects from the consolidated JSON file
with open("aspects.json", "r") as f:
    aspects = json.load(f)

# Generate super prompt using the provided preferences
super_prompt = generate_super_prompt(aspects)

# Initialize conversation messages with system message (super prompt)
messages = [
    {
        "role": "system",
        "content": super_prompt
    }
]

# Get the chatbot to make the first move
messages.append({"role": "assistant", "content": get_response(messages)})
print(f"Attacker: {messages[-1]['content']}")

# Chat loop
while True:
    user_input = input("Victim: ")
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": get_response(messages)})
    print(f"Attacker: {messages[-1]['content']}")
