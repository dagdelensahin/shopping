"""Item/Product model."""
from datetime import datetime
from ..database import db


class Item(db.Model):
    """Item/Product entity for shopping app."""
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    
    # Relationships
    order_items = db.relationship('OrderItem', back_populates='item', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Item {self.name}>'
