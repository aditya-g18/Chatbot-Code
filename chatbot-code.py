# Basic Chatbot Code in Python

def chatbot_response(user_input):
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! How can I assist you?",
        "how are you": "I'm just a bot, but thanks for asking! How are you?",
        "what is your name": "I'm ChatEasy, your friendly chatbot!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome!",
    }
    
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm sorry, I didn't understand that. Can you rephrase?"

print("Welcome to ChatEasy! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatEasy: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("ChatEasy:", response)
