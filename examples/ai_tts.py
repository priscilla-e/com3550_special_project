import os
import openai
from dotenv import load_dotenv
import tempfile
import pygame

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in environment variables. Please add it to your .env file.")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

def generate_speech(text, voice="alloy", model="tts-1"):
    """
    Generate speech from text using OpenAI's TTS API.
    
    Args:
        text (str): The text to convert to speech
        voice (str): The voice to use (alloy, echo, fable, onyx, nova, or shimmer)
        model (str): The TTS model to use
        
    Returns:
        bytes: The audio data
    """
    try:
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        return response.content
    except Exception as e:
        print(f"Error generating speech: {str(e)}")
        return None

def play_audio(audio_data):
    """
    Play the generated audio using pygame.
    
    Args:
        audio_data (bytes): The audio data to play
    """
    if audio_data is None:
        return
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(audio_data)
        temp_filename = temp_file.name
    
    # Load and play the audio
    try:
        pygame.mixer.music.load(temp_filename)
        pygame.mixer.music.play()
        
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing audio: {str(e)}")
    finally:
        # Clean up the temporary file
        pygame.mixer.music.unload()
        os.unlink(temp_filename)

def main():
    print("Welcome to the AI Text-to-Speech Bot!")
    print("Type 'quit' or 'exit' to end the program.")
    print("Available voices: alloy, echo, fable, onyx, nova, shimmer")
    
    # Default voice
    current_voice = "alloy"
    
    while True:
        user_input = input("\nEnter text to speak (or 'voice [name]' to change voice): ")
        
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        # Check if user wants to change voice
        if user_input.lower().startswith("voice "):
            new_voice = user_input.lower().split("voice ")[1].strip()
            if new_voice in ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]:
                current_voice = new_voice
                print(f"Voice changed to {current_voice}")
            else:
                print("Invalid voice. Available voices: alloy, echo, fable, onyx, nova, shimmer")
            continue
        
        # Generate and play speech
        print(f"Generating speech with voice '{current_voice}'...")
        audio_data = generate_speech(user_input, voice=current_voice)
        if audio_data:
            print("Playing audio...")
            play_audio(audio_data)

if __name__ == "__main__":
    main()