from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from coupon.db_config.base_config import Base
from coupon.db_config.base_config import engine


class Signup(Base):
    __tablename__ = "signup"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column('username', String(45), unique=True, index=False)
    password = Column('password', String(45), unique=False, index=False)


class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(45), unique=False, index=False)
    password = Column(String(45), unique=False, index=False)
    passphrase = Column(String(200), unique=False, index=False)
    approved_date = Column(Date, unique=False, index=False)

    users = relationship('User', back_populates='login', uselist=False)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, ForeignKey('login.id'), primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(45), unique=False, index=False)
    lastname = Column(String(45), unique=False, index=False)
    balance = Column(Float, unique=False, index=False)

    login = relationship('Login', back_populates="users")


class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Float, unique=False, index=False)
    capacity_of_use = Column(Integer, unique=False, index=False)
    status = Column(Integer, unique=False, index=False)
    expire_time = Column(Date, unique=False, index=False)
    code = Column(String(20), unique=True, index=True)


class Coupon_User(Base):
    __tablename__ = 'coupon_user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    coupon_id = Column(Integer, ForeignKey('coupons.id'), unique=False, index=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=False, index=False)


Base.metadata.create_all(engine)
