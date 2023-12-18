#!/usr/bin/python3
""" DB Storage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    """ This class manages storage of hbnb models in MySQL """

    __engine = None
    __session = None

    def __init__(self):
        """ Creates the engine, session, and drops tables if in test mode """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current database session for all objects of a given class"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            for class_name in classes:
                objs = self.__session.query(classes[class_name]).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Adds the object to the current session """
        # if obj not in self.__session:
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current session """
        try:
            self.__session.commit()
        except Exception as e:
            print(e)
            self.__session.rollback()

    def delete(self, obj=None):
        """ Deletes obj from the current session if not None """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database and creates a session """
        Base.metadata.create_all(self.__engine)
        # self.__session = scoped_session(sessionmaker(
        #     bind=self.__engine, expire_on_commit=False))

    def close(self):
        """ Calls close() on the private session attribute """
        self.__session.remove()
