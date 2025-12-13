"""Routes package - all API endpoints."""
from .items import items_bp
from .categories import categories_bp
from .orders import orders_bp
from .login import login_bp

__all__ = ['items_bp', 'categories_bp', 'orders_bp', 'login_bp']
