import requests
from typing import Optional


class DictionaryApp:
    """
    A class that works with the Merriam-Webster Dictionary API to fetch word definitions.
    This demonstrates how to work with REST APIs in Python.

    # TODO: Add your API key below before running the program.
    """
    def __init__(self):
        # API credentials and endpoint configuration
        self.api_key = None # TODO: Add your API key here
        self.base_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

    def get_word_definition(self, word: str) -> Optional[dict]:
        """
        Fetches the definition of a given word from the Merriam-Webster API.
        
        Args:
            word (str): The word to look up
            
        Returns:
            Optional[dict]: A dictionary containing the word, its definitions, and part of speech.
                          Returns None if the word is not found or if there's an error.
        """
        try:
            # Make HTTP GET request to the API
            response = requests.get(
                f"{self.base_url}{word}",
                params={"key": self.api_key}
            )
            # Raise an exception for bad status codes (e.g., 404, 500)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Check if the response is empty or if the first element is not a dictionary
            if not data or not isinstance(data[0], dict):
                return None

            # Extract definitions from the response
            definitions = []
            for entry in data:
                if "shortdef" in entry:
                    definitions.extend(entry["shortdef"])

            # Return a dictionary with the word, definitions, and part of speech
            return {
                "word": word,
                "definitions": definitions,
                "part_of_speech": data[0].get("fl", "N/A")
            }

        except requests.RequestException as e:
            # Handle any API request error
            print(f"Error fetching definition: {e}")



def main():
    """
    Main program loop that handles user interaction.
    Demonstrates input/output operations and program flow control.
    """
    app = DictionaryApp()

    # Print welcome banner
    print("Welcome to the A-Level Dictionary App!")
    print("\n" + "="*50)
    print("Welcome to the Dictionary App!")
    print()
    print("Type a word and press Enter to get its definition")
    print("Type 'quit' to exit the program")
    print("="*50 + "\n")


    while True:
        # Get user input
        word = input("\nEnter a word (or 'quit' to exit): ").strip()

        if word.lower() == 'quit':
            break

        result = app.get_word_definition(word)

        if result:
            # Print results in a structured format
            print("\n" + "-"*50)
            print(f"📚 Word: {result['word'].upper()}")
            print(f"🔤 Part of Speech: {result['part_of_speech']}")
            print("\n📑 Definitions:")

            # Print the first 5 definitions, or all if less than 5
            for i, definition in enumerate(result['definitions'][:min(5, len(result['definitions']))], 1):
                print(f"  {i}. {definition}")
            print("-"*50 + "\n")
        else:
            print("\n" + "-"*50)
            print(f"❌ Sorry, couldn't find the definition for '{word}'")
            print("-"*50 + "\n")


if __name__ == "__main__":
    main()