
def get_bot_response(user_message):
    
    user_message = user_message.strip().lower()

    # if-elif-else conditional logic mapping inputs to rules
    if "hello" in user_message or "hi" in user_message:
        return "🤖 Bot: Hi! How can I help you today?"
    
    elif "how are you" in user_message:
        return "🤖 Bot: I'm fine, thanks! Just running smoothly on Python code."
    
    elif "your name" in user_message:
        return "🤖 Bot: I am BasicBot, your rule-based assistant."
    
    elif "bye" in user_message or "goodbye" in user_message:
        return "🤖 Bot: Goodbye! Have a fantastic day!"
    
    else:
        return "🤖 Bot: I'm sorry, I don't quite understand that response yet. Try saying 'hello', 'how are you', or 'bye'."

def main():
    print("--- 💬 Welcome to the Basic Chatbot 💬 ---")
    print("Type your message below. Type 'bye' to exit the conversation.\n")
    
    
    while True:
        user_input = input("You: ")
        
        
        response = get_bot_response(user_input)
        print(response)
        
        
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    main()