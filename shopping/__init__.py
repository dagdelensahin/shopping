"""Top-level package for shopping."""

__all__ = ["greet", "__version__"]

__version__ = "0.1.0"

from .core import greet  # re-export simple API
