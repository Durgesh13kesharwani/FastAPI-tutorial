from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)  
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator= relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    # Ensure that the password is hashed before storing it
    # You can use a library like bcrypt or passlib to hash the password

    blogs = relationship("Blog", back_populates="creator")