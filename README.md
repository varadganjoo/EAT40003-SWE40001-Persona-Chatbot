# Cybersecurity Simulation Chatbot

This project, developed by "Persona Chatbot Group 6", simulates a conversation with a fictional cyber attacker named "Attacker" using OpenAI's GPT-3.5-turbo. The purpose of this chatbot is to demonstrate the potential of AI-driven dialogues in cybersecurity scenarios for educational and awareness purposes.

## Features

- Engage in a realistic conversation with a fictional attacker.
- Utilizes OpenAI's GPT-3.5-turbo model for natural language processing.
- Customizable system prompt to set the initial context for the conversation.
- Modular code design for easy modifications and extensions.
- Ability to tune GPT's behavior by adjusting parameters like `temperature`, `frequency_penalty`, etc.

## Getting Started

### Prerequisites

- Python 3.9+
- OpenAI Python Client: Install using `pip install openai`

### Setup

1. Clone the repository:

\```bash
git clone https://github.com/varadganjoo/EAT40003-SWE40001-Persona-Chatbot.git
cd EAT40003-SWE40001-Persona-Chatbot
\```

2. Replace `YOUR_API_KEY` in the `openai_chatbot()` function with your actual OpenAI API key.
3. (Optional) Modify the `content.txt` file to customize the system's initial prompt.

### Running the Chatbot

Execute the following command:

\```bash
python FYP_Project.py
\```

This will initiate the chatbot, and you'll be engaged in a conversation with the "Attacker".

### Tuning the Chatbot

You can adjust the behavior of the GPT model by tweaking the following parameters:

- `temperature`: Higher values (e.g., 0.8) make the output more random, while lower values (e.g., 0.2) make it more deterministic.
- `frequency_penalty`: Adjusts the penalty for using frequent tokens. You can set values between -2 and 2.
- `presence_penalty`: Adjusts the penalty for using new tokens. You can set values between -2 and 2.

Feel free to experiment with these parameters to get the desired conversational behavior from the chatbot.

## Usage Notes

- The conversation is purely fictional and is intended for demonstrative purposes.
- Always handle API keys with care. Do not expose them in your codebase or public repositories.

## Acknowledgments

- OpenAI for their incredible GPT models and API.
- Retrospect Labs for their valuable contributions and insights.
- Persona Chatbot Group 6 for the development of this project.
