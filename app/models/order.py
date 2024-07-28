from . import BASE
from sqlalchemy import Column, Integer, Float, Text, ForeignKey, String, Float, Text, DateTime
from sqlalchemy.orm import relationship


class Order(BASE):
    __tablename__ = "orders"



    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)
    item = relationship("Ordered_items", backref="order")


class Ordered_items(BASE):    
    __tablename__ = "ordered_items"


    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, ForeignKey("carts.quantity"), nullable=False)

