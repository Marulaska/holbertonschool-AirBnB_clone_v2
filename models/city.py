#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ City class """
    __tablename__ = 'cities'

    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
