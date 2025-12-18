"""Item routes - handles all item-related endpoints."""
from flask import Blueprint, jsonify, request
from ..models import db, Category

categories_bp = Blueprint('categories', __name__, url_prefix='/api/categories')


@categories_bp.route('', methods=['GET'])
def get_categories():
    """Get all categories from database."""
    try:
        categories = Category.query.all()
        return jsonify([{
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at.isoformat()
        } for category in categories]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching items", "error": str(e)}), 500
    

@categories_bp.route('', methods=['POST'])
def add_category():
    """Add a new category to the database."""
    data = request.json
    print(data)

    if not data:
        return jsonify({"message": "No data provided"}), 400
    if not data['category']['name']:
        return jsonify({"message": "Missing required field: name"}), 400
    
    try:
        category = Category(
            name=data['category']['name'],
            description=data['category']['description'] if 'category' in data and 'description' in data['category'] else ""
        )
        db.session.add(category)
        db.session.commit()
        return jsonify({"message": "Category added", "category": {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at.isoformat()
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding category", "error": str(e)}), 500
    

@categories_bp.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Get a specific category by ID."""
    try:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"message": "Category not found"}), 404
        return jsonify({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at.isoformat()
        }), 200
    except Exception as e:
        return jsonify({"message": "Error fetching category", "error": str(e)}), 500
    

@categories_bp.route('/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Delete a specific category by ID."""
    try:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"message": "Category not found"}), 404
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting category", "error": str(e)}), 500
    

@categories_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):   
    """Update a specific category by ID."""
    data = request.json
    
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    try:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"message": "Category not found"}), 404
        
        category.name = data.get("name", category.name)
        category.description = data.get("description", category.description)
        
        db.session.commit()
        return jsonify({"message": "Category updated", "category": {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at.isoformat()
        }}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating category", "error": str(e)}), 500
    

@categories_bp.route('/<int:category_id>/items', methods=['GET'])
def get_items_by_category(category_id):
    """Get all items in a specific category."""
    try:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"message": "Category not found"}), 404
        
        items = category.items  # Assuming a relationship is defined in Category model
        return jsonify([{
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "quantity_in_stock": item.quantity_in_stock
        } for item in items]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching items", "error": str(e)}), 500   
