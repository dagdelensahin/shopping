"""Category model."""
from datetime import datetime
from ..database import db


class Category(db.Model):
    """Category entity for organizing items."""
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False, index=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('Item', backref='category_rel', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'
