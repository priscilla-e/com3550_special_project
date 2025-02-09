from flask import request
from app.user import user_bp
from app.models.user import User


# GET '/api/users
@user_bp.route('/users', methods=['GET'])
def get_users():
    """Get all users.

    Optional query parameters:
    - id: filter by user id
    - username: filter by username
    """
    # Get request parameters
    id = request.args.get('id')
    username = request.args.get('username')

    # Query the database for all users
    query = User.query

    # Filter users by the request parameters if provided
    if id:
        query = query.filter(User.id == id)
    if username:
        query = query.filter(User.username == username)
        
    # Return the users data as JSON with appropriate HTTP status code
    users = query.all() 
    users_data = [user.to_dict() for user in users]
    return {'users': users_data}, 200


# POST '/api/user'
@user_bp.route('/user', methods=['POST'])
def new_user():
    """Read a new user.
    """
    # Extract JSON data from the request
    data = request.json
    
    # TODO: Validate required fields (username, email, etc.)
    
    # TODO: Check if user already exists (e.g., by username or email)
    
    # TODO: Create new user in database
    
    # TODO: Return new user data with 201 status code
    

# GET '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a user by their ID.
    """
    # TODO: Check if user exists in database
    
    # TODO: Query database for user with user_id
    
    # TODO: If user not found, return 404 error

    # TODO: Return user data as JSON with 200 status code


# PUT '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's password.
    """
    # Get and validate JSON data from request
    data = request.json
    if not data:
        return {'error': 'No data provided'}, 400

    # TODO: Check if user exists in database
    
    # TODO: Update user password in database
    
    # TODO: Return updated user data with 200 status code
    # If user not found, return 404 error
    

# DELETE '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user.
    """
    # TODO: Check if user exists in database
    
    # TODO: Delete user from database
    
    # TODO: Return deleted user data with 200 status code
    # If user not found, return 404 error
