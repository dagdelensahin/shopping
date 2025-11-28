from flask import Blueprint, jsonify, request
from ..models import db, Order, OrderItem, Item


orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@orders_bp.route('', methods=['GET'])
def get_orders():
    """Get all orders from database."""
    try:
        orders = Order.query.all()
        return jsonify([{
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat(),
            "order_items": [{
                "item_id": oi.item_id,
                "quantity": oi.quantity,
                "price": oi.price
            } for oi in order.order_items]
        } for order in orders]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching orders", "error": str(e)}), 500
    

@orders_bp.route('', methods=['POST'])
def add_order():
    """Add a new order to the database."""
    data = request.json
    
    if not data:
        return jsonify({"message": "No data provided"}), 400
    if not data.get("user_id") or not data.get("order_items"):
        return jsonify({"message": "Missing required fields: user_id and order_items"}), 400
    
    try:
        order = Order(
            user_id=int(data["user_id"]),
            total_price=0.0,
            status='pending'
        )
        db.session.add(order)
        db.session.flush()  # Get order ID before committing
        
        total_price = 0.0
        for oi in data["order_items"]:
            item = Item.query.get(oi["item_id"])
            if not item:
                db.session.rollback()
                return jsonify({"message": f"Item with ID {oi['item_id']} not found"}), 404
            order_item = OrderItem(
                order_id=order.id,
                item_id=item.id,
                quantity=int(oi["quantity"]),
                price=item.price
            )
            total_price += item.price * int(oi["quantity"])
            db.session.add(order_item)
        
        order.total_price = total_price
        db.session.commit()
        
        return jsonify({"message": "Order added", "order": {
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat()
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding order", "error": str(e)}), 500
    

@orders_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get a specific order by ID."""
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        return jsonify({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat(),
            "order_items": [{
                "item_id": oi.item_id,
                "quantity": oi.quantity,
                "price": oi.price
            } for oi in order.order_items]
        }), 200
    except Exception as e:
        return jsonify({"message": "Error fetching order", "error": str(e)}), 500
    


@orders_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update a specific order by ID."""
    data = request.json
    
    if not data:
        return jsonify({"message": "No data provided"}), 400
    
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        
        if "status" in data:
            order.status = data["status"]
        
        db.session.commit()
        return jsonify({"message": "Order updated", "id": order.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating order", "error": str(e)}), 500   
    
@orders_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete a specific order by ID."""
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting order", "error": str(e)}), 500
    

@orders_bp.route('/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    """Get all orders for a specific user by user ID."""
    try:
        orders = Order.query.filter_by(user_id=user_id).all()
        return jsonify([{
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
            "created_at": order.created_at.isoformat(),
            "updated_at": order.updated_at.isoformat(),
            "order_items": [{
                "item_id": oi.item_id,
                "quantity": oi.quantity,
                "price": oi.price
            } for oi in order.order_items]
        } for order in orders]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching user's orders", "error": str(e)}), 500
    

@orders_bp.route('/<int:order_id>/items', methods=['GET'])
def get_order_items(order_id):
    """Get all items for a specific order by order ID."""
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        return jsonify([{
            "item_id": oi.item_id,
            "quantity": oi.quantity,
            "price": oi.price
        } for oi in order.order_items]), 200
    except Exception as e:
        return jsonify({"message": "Error fetching order items", "error": str(e)}), 500
    

@orders_bp.route('/<int:order_id>/items', methods=['POST'])
def add_order_item(order_id):
    """Add an item to a specific order by order ID."""
    data = request.json
    
    if not data:
        return jsonify({"message": "No data provided"}), 400
    if not data.get("item_id") or not data.get("quantity"):
        return jsonify({"message": "Missing required fields: item_id and quantity"}), 400
    
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        
        item = Item.query.get(data["item_id"])
        if not item:
            return jsonify({"message": "Item not found"}), 404
        
        order_item = OrderItem(
            order_id=order.id,
            item_id=item.id,
            quantity=int(data["quantity"]),
            price=item.price
        )
        order.total_price += item.price * int(data["quantity"])
        
        db.session.add(order_item)
        db.session.commit()
        
        return jsonify({"message": "Order item added", "order_item": {
            "item_id": order_item.item_id,
            "quantity": order_item.quantity,
            "price": order_item.price
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding order item", "error": str(e)}), 500