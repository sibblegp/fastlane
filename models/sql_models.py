__author__ = 'gsibble'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, DateTime
from sqlalchemy import create_engine

from config import settings

import datetime

ENGINE = create_engine(settings.SQL_URI)

SESSION_MAKER = sessionmaker()
SESSION_MAKER.configure(bind=ENGINE)

BASE = declarative_base()
SESSION = SESSION_MAKER(autocommit=False,
                        autoflush=False,
                        bind=ENGINE)

def add(objects):
    if type(objects) == list:
        for object in objects:
            SESSION.add(object)
    else:
        SESSION.add(objects)

def commit():
    SESSION.commit()

class User(BASE):
    __tablename__ = 'users'

    #Columns
    id = Column(Integer, primary_key=True)
    urban_airship_alias = Column(String(50), nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))

class Device(BASE):
    __tablename__ = 'devices'

    #Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    urban_airship_channel = Column(String(50), nullable=False)

    #Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'))

    #Relationships
    user = relationship('User', backref=backref('devices'))

class Merchant(BASE):
    __tablename__ = 'merchants'

    #Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    @classmethod
    def get(cls, merchant_id):
        return SESSION.query(cls).get(merchant_id)

class Transaction(BASE):
    __tablename__ = 'transactions'

    #Columns
    id = Column(Integer, primary_key=True)
    hash = Column(String(50))
    merchant_transaction_id = Column(String(50), nullable=False)
    amount = Column(DECIMAL, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow())
    completed = Column(DateTime)

    #Foreign Keys
    merchant_id = Column(Integer, ForeignKey('merchants.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    #Relationships
    merchant = relationship('Merchant', backref=backref('transactions', order_by=created))
    user = relationship('User', backref=backref('transactions', order_by=created))

    @classmethod
    def create(cls, merchant, amount, merchant_transaction_id):
        new_transaction = cls(amount=amount,
                              merchant=merchant,
                              merchant_transaction_id=merchant_transaction_id)
        add(new_transaction)
        commit()

        return new_transaction


def reset_db():
    session = SESSION_MAKER()
    BASE.metadata.drop_all(ENGINE)
    BASE.metadata.create_all(ENGINE)
    new_merchant = Merchant()
    new_merchant.name = 'Test Merchant'
    session.add(new_merchant)
    session.commit()
    session.close()