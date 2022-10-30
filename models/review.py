#!/usr/bin/python3
from models.base_model import BaseModel
"""a Review class"""
class Review(BaseModel):
    """holds reviews from users"""
    place_id = ""
    user_id = ""
    text = ""
