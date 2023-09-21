import os
import openai
import time

# Set your API key as an environment variable or load it from a file
os.environ["OPENAI_API_KEY"] = "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"

# Authenticate with OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

def get_response(prompt, user_input):
    # Set up API request parameters
    parameters = {
        "engine": "text-davinci-002",
        "prompt": f"{prompt}\nVictim: {user_input}\nAttacker: ",
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }

    # Use OpenAI API to generate response
    response = openai.Completion.create(**parameters)

    # Extract response text from API response
    response_text = response.choices[0].text.strip()

    return response_text

def generate_backstory(attacker_type, attack_type, victim_name):
    # Generate backstory using GPT-3
    prompt = f"Generate a backstory for a {attacker_type} cyber attacker who used a {attack_type} attack against {victim_name}. Use first person language and pretend you are speaking directly to me about your backstory"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    backstory = response.choices[0].text.strip()

    # Generate demands using GPT-3
    prompt = f"Generate demands for the {attacker_type} cyber attacker who used a {attack_type} attack against {victim_name}. Use first person language and pretend you are speaking directly to me about your demands"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    demands = response.choices[0].text.strip()

    # Generate initial prompt
    prompt = f"You are a {attacker_type} cyber attacker who used a {attack_type} attack against my company, {victim_name}. {backstory} {demands}. You are speaking to me through Whats App. \nAttacker: "

    return prompt

# Prompt user for information about the cyber attack
attacker_type = input("What type of cyber attacker are you? ")
attack_type = input("What cyber attack did you use against your victim? ")
victim_name = input("Who is your victim? ")

# Generate initial prompt using the provided information
prompt = generate_backstory(attacker_type, attack_type, victim_name)

# Generate response from model without context
response = get_response(prompt, "")

# Print attacker's initial message
print(f"Attacker: {response}")

while True:
    # Prompt user for input
    user_input = input("Victim: ")

    # Generate response from model with context
    response = get_response(prompt, user_input)

    # Print response
    print(f"Attacker: {response}")

    # Wait for a second
    time.sleep(1)

    # Update the prompt with the new response
    prompt += f"Victim: {user_input}\nAttacker: {response}"
