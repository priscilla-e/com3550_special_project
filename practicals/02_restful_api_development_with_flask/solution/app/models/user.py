"""
User model

This module defines the User model class which represents user data in the database.

Attributes:
    id (int): primary key - The unique identifier for the user 
    username (str): The unique username for the user
    password (str): The user's password (should be hashed in production)
"""
from app.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from datetime import datetime


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<User "{self.id}">'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }