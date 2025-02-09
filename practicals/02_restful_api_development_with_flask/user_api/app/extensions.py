from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

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
Initialize the SQLAlchemy extension for our Flask application.
This allows us to create and manage our database models
"""
db = SQLAlchemy()
