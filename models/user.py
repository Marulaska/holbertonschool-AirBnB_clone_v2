#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class"""
    __tablename__ = 'users'

    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
