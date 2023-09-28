import os
import openai
import json
import time

# Set your API key as an environment variable or load it from a file
os.environ["OPENAI_API_KEY"] = "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"

# Authenticate with OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

def get_response(prompt, user_input):
    parameters = {
        "engine": "text-davinci-002",
        "prompt": f"{prompt}\nVictim: {user_input}\nAttacker: ",
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }
    response = openai.Completion.create(**parameters)
    return response.choices[0].text.strip()

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

    super_prompt = f"You are {actors} who used a {threats} against {victim}. {background} {incidents} {behaviors} {evidence} {flow} {conditions} \nAttacker: "
    return super_prompt

# Load aspects from the consolidated JSON file
with open("aspects.json", "r") as f:
    aspects = json.load(f)

# Generate super prompt using the provided preferences
prompt = generate_super_prompt(aspects)

# Chat loop
while True:
    user_input = input("Victim: ")
    response = get_response(prompt, user_input)
    print(f"Attacker: {response}")
    time.sleep(1)
    prompt += f"Victim: {user_input}\nAttacker: {response}"