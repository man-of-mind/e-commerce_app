from enum import unique
from sqlalchemy import Column, Boolean, DateTime, ForeignKey, String, Integer, Text
from .database import Base
from sqlalchemy.orm import relationship

class All_categories(Base):
    __tablename__ = "all_categories" 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True)
      
class Sub_catagories(Base):
    __tablename__ = "sub_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40))
    category_type = Column(String(40), ForeignKey("all_categories.name"))
    
class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True)
    sub_category_type = Column(String(40))
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id"))
   
class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100))
    type_id = Column(Integer, ForeignKey("type.id"))
    price = Column(Integer)
    