"""Item routes - handles all item-related endpoints."""
from flask import Blueprint, jsonify, request
from ..models import db, Item

items_bp = Blueprint('items', __name__, url_prefix='/api/items')


@items_bp.route('', methods=['GET'])
def get_items():
    """Get all items from database."""
    try:
        items = Item.query.all()
        return jsonify([{
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "quantity_in_stock": item.quantity_in_stock,
            "category": item.category
        } for item in items]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching items", "error": str(e)}), 500


@items_bp.route('', methods=['POST'])
def add_item():
    """Add a new item to the database."""
    data = request.json
    
    if not data:
        return jsonify({"message": "No data provided"}), 400
    if not data.get("name") or not data.get("price"):
        return jsonify({"message": "Missing required fields: name and price"}), 400
    
    try:
        item = Item(
            name=data["name"],
            description=data.get("description", ""),
            price=float(data["price"]),
            quantity_in_stock=int(data.get("quantity_in_stock", 0)),
            category=data.get("category", "")
        )
        db.session.add(item)
        db.session.commit()
        return jsonify({"message": "Item added", "item": {
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "quantity_in_stock": item.quantity_in_stock,
            "category": item.category
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding item", "error": str(e)}), 500


@items_bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item by ID."""
    try:
        item = Item.query.get(item_id)
        if not item:
            return jsonify({"message": "Item not found"}), 404
        return jsonify({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "quantity_in_stock": item.quantity_in_stock,
            "category": item.category
        }), 200
    except Exception as e:
        return jsonify({"message": "Error fetching item", "error": str(e)}), 500


@items_bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an item."""
    data = request.json
    
    try:
        item = Item.query.get(item_id)
        if not item:
            return jsonify({"message": "Item not found"}), 404
        
        if "name" in data:
            item.name = data["name"]
        if "description" in data:
            item.description = data["description"]
        if "price" in data:
            item.price = float(data["price"])
        if "quantity_in_stock" in data:
            item.quantity_in_stock = int(data["quantity_in_stock"])
        if "category" in data:
            item.category = data["category"]
        
        db.session.commit()
        return jsonify({"message": "Item updated", "id": item.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating item", "error": str(e)}), 500


@items_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item."""
    try:
        item = Item.query.get(item_id)
        if not item:
            return jsonify({"message": "Item not found"}), 404
        
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Item deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting item", "error": str(e)}), 500
