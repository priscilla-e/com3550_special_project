import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in environment variables. Please add it to your .env file.")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

def chat_with_ai(messages, model="gpt-3.5-turbo"):
    """
    Send messages to the OpenAI API and get a response.
    
    Args:
        messages (list): List of message dictionaries with role and content
        model (str): The model to use for chat completion
        
    Returns:
        str: The AI's response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the AI Chat Bot!")
    print("Type 'quit' or 'exit' to end the conversation.")
    
    # Initialize conversation history with system message
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        # Get AI response based on the entire conversation history
        ai_response = chat_with_ai(conversation_history)
        
        # Add AI response to conversation history
        conversation_history.append({"role": "assistant", "content": ai_response})
        
        print(f"\nAI: {ai_response}")

if __name__ == "__main__":
    main()

