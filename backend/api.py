"""Simple Flask API for the shopping project with CORS enabled."""
from flask import Flask, jsonify, request
from flask_cors import CORS
from .core import greet


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.get("/api/hello")
    def hello():
        """Return a greeting message. Query param: `name`"""
        name = request.args.get("name", "World")
        return jsonify({"message": greet(name)})

    @app.get("/api/items")
    def items():
        """Return a small list of sample items."""
        sample = [
            {"id": 1, "name": "Apple", "price": 0.5},
            {"id": 2, "name": "Milk", "price": 1.2},
        ]
        return jsonify(sample)

    return app


def main():
    app = create_app()
    # Run development server on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
