"""Simple Flask API for the shopping project with CORS enabled."""
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
try:
    import pymysql
except ImportError:
    pymysql = None
from .core import greet
from .models import db, User, Item, Order, OrderItem, Category
from .routes import items_bp, categories_bp


def get_db_config():
    """Get database configuration from environment variables or defaults."""
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'port': int(os.getenv('DB_PORT', 3306)),
    }


def create_database_if_not_exists():
    """Create the shopping database if it doesn't exist."""
    try:
        config = get_db_config()
        connection = pymysql.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            port=config['port'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("CREATE DATABASE IF NOT EXISTS shopping CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
                connection.commit()
        finally:
            connection.close()
    except pymysql.Error as e:
        print(f"Warning: Could not create database: {e}")


def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Create database if it doesn't exist
    create_database_if_not_exists()
    
    # Database configuration from environment or defaults
    config = get_db_config()
    # Build URI without unsupported parameters
    db_uri = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/shopping?charset=utf8mb4"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'connect_args': {
            'charset': 'utf8mb4',
        },
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True,
    }
    
    # Initialize database
    db.init_app(app)
    CORS(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(items_bp)
    app.register_blueprint(categories_bp)

    @app.get("/api/hello")
    def hello():
        """Return a greeting message. Query param: `name`"""
        name = request.args.get("name", "World")
        return jsonify({"message": greet(name)})
    return app


def main():
    app = create_app()
    # Run development server on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
