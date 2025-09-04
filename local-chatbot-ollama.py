import ollama

def simple_chatbot(model='phi3:mini'):
    """
    A basic interactive chatbot loop using Ollama.
    Type 'exit' to quit the conversation.
    """
    # Initialize conversation history
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        }
    ]
    
    print("Chatbot ready! Type 'exit' to quit.")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Add user message to history
        messages.append({
            'role': 'user',
            'content': user_input
        })
        
        # Generate response from the model
        response = ollama.chat(
            model=model,
            messages=messages
        )
        
        # Extract and print AI response
        ai_response = response['message']['content']
        print(f"Chatbot: {ai_response}")
        
        # Add AI response to history for context
        messages.append({
            'role': 'assistant',
            'content': ai_response
        })

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()