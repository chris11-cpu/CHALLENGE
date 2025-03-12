# Step 1: Initialization
def get_bot_response(user_message):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "tell me about place": "Sure! I can help with places. Tell me more!",
        "bye": "Goodbye! Have a great day!"
    }
    # Convert user input to lowercase to ensure case-insensitive matching
    user_message = user_message.lower()
    
    # If the message exists in responses, return the response, else default
    return responses.get(user_message, "Sorry, I didn't understand that.")

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    # Step 4: Main interaction loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        # Get bot response and print it
        print("Chatbot:", get_bot_response(user_input))

# Step 5: Exit the program
if _name_ == "_main_":
    main()
