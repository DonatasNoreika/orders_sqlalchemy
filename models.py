from sqlalchemy import (Column,
                        Integer,
                        String,
                        Float,
                        DateTime,
                        ForeignKey,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///ecommerce.db')
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    last_name = Column("Lastname", String)
    email = Column("Email", String)


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    price = Column("Price", Float)


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    date = Column("Date", DateTime)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer")
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship("Status")
    order_line = relationship("OrderLine")

    def __repr__(self):
        return f"{self.id}: date - {self.date}, customer - {self.customer.name} {self.customer.last_name}, status - {self.status.name}"


class OrderLine(Base):
    __tablename__ = "order_line"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship("Order")
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product")
    qty = Column("Quantity", Integer)

Base.metadata.create_all(engine)
