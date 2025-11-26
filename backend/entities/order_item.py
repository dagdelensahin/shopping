"""OrderItem model representing many-to-many between orders and items."""
from datetime import datetime
from ..database import db


class OrderItem(db.Model):
    """OrderItem entity - many-to-many relationship between Order and Item."""
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False, index=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False)  # Price at time of order
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    order = db.relationship('Order', back_populates='order_items')
    item = db.relationship('Item', back_populates='order_items')
    
    def __repr__(self):
        return f'<OrderItem order_id={self.order_id} item_id={self.item_id}>'
