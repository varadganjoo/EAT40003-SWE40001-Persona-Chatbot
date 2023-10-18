import os
import openai

def read_content_from_file(filename="content.txt"):
    with open(filename, 'r') as file:
        return file.read()

def openai_chatbot():
    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Initial setup
    content = read_content_from_file()
    messages = [{"role": "system", "content": content}]
    
    # Have the model initiate the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.22,
        presence_penalty=0.15
    )
    assistant_response = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": assistant_response})
    print(f"Attacker: {assistant_response}")
    
    while True:
        # Getting user input
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        
        # Getting model's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=messages,
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0.22,
            presence_penalty=0.15
        )
        assistant_response = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": assistant_response})
        
        print(f"\nAttacker: {assistant_response}")

# Uncomment the below line to run the chatbot
openai_chatbot()