import openai

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Initialize the conversation with a system message
conversation = [
    {"role": "system", "content": "you are my personal psyciatrist. you have a bhaelors degree on arts in pilosophy. you are a phd holder in psycology. you are here to help me maitain  my mental stability and you should help me to keep calm."}
]

while True:
    # Prompt the user for input
    user_input = input("You: ")

    # Add user's message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Generate a response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Extract the model's reply
    assistant_reply = response['choices'][0]['message']['content']

    # Print the model's response
    print("AI: " + assistant_reply)

    # Add the model's reply to the conversation
    conversation.append({"role": "assistant", "content": assistant_reply})
