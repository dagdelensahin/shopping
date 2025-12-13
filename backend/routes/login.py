from flask import Blueprint, jsonify, request
from backend.services import AuthService


login_bp = Blueprint('login', __name__, url_prefix='/api/login')



@login_bp.route('', methods=['POST'])
def login():
    """Handle user login."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
    auth_service = AuthService(username, password)
    token = auth_service.authenticate(username, password)
    
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials.'}), 401
