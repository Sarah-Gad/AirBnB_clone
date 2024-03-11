# models/__init__.py
"""This module creates a FileStorage instance"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
