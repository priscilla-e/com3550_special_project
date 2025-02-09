from flask import request
from app.user import user_bp
from app.models.user import User
from app.extensions import db


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
    """Create a new user.
    """
    # Extract JSON data from the request
    data = request.json
    
    # Validate required fields
    # Note: This is a simple validation. In a real-world application, you should use a more robust validation library
    if not data or 'username' not in data or 'password' not in data:
        return {'error': 'Missing required fields'}, 400
        
    # Check if user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return {'error': 'Username already exists'}, 409
        
    # Create new user in database
    # Note: In a real-world application, you should hash the password before storing it in the database
    user = User(
        username=data['username'],
        password=data['password']
    )
    db.session.add(user)
    db.session.commit()
    
    # Return new user data with 201 status code
    return {
        'message': 'User created successfully',
        'user': user.to_dict()
    }, 201


# GET '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a user by their ID.
    """
    # Query database for user with user_id
    user = User.query.get(user_id)
    
    # If user not found, return 404 error
    if not user:
        return {'error': 'User not found'}, 404
        
    # Return user data as JSON with 200 status code
    return {'user': user.to_dict()}, 200


# PUT, PATCH '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's password.
    """
    # Get and validate JSON data from request
    data = request.json
    if not data or 'password' not in data:
        return {'error': 'Missing required field'}, 400

    # Check if user exists in database
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
    
    #Update user password in database
    user.password = data['password']
    db.session.commit()
    
    # Return updated user data with 200 status code
    return {
        'message': 'User updated successfully', 
        'user': user.to_dict()
    }, 200


# DELETE '/api/user/<user_id>'
@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user.
    """
    # Check if user exists in database
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}, 404
        
    # Delete user from database
    db.session.delete(user)
    db.session.commit()
    
    # Return deleted user data with 200 status code
    return {
        'message': 'User deleted successfully',
        'user': user.to_dict()
    }, 200
