import os
from flask_cors import CORS
from openai import OpenAI

"""
Initialize CORS (Cross-Origin Resource Sharing) extension for our Flask application.
This allows us to specify which origins can access our API
- (*) allows all origins to access our API

Example:
- Allowing a frontend application (e.g., React) running on one domain (http://localhost:3000 )
  to make API requests to this Flask backend running on a different domain (http://localhost:5000/api/)
"""
cors = CORS(origin="*")


"""
Initialize the OpenAI client

Ensure you have the OPENAI_API_KEY environment variable set in your .env file
"""
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "default"))