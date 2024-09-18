from sqlalchemy import create_engine,  Column, Integer, String,ForeignKey 
from sqlalchemy.orm import declarative_base ,sessionmaker,relationship


engine = create_engine('sqlite:///database.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contacts = Column(Integer)
    orders = relationship('Order', back_populates='customer')

    # def __repr__(self):
    #     return f"<Customer(id='{self.id}', customer_name='{self.customer_name}', contacts='{self.contacts}')>"
class Laptop(Base):
    __tablename__ = 'laptops'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specification = Column(String)
    price = Column(Integer)
   
    orders= relationship('Order', back_populates='laptop')
    
    
    # def __repr__(self):
    #     return f"<Laptops(id='{self.id}', laptop_name='{self.laptop_name}', specification='{self.specification}', price='{self.price}')>"
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    laptop_id = Column(Integer, ForeignKey('laptops.id'))
    quantity = Column(Integer,default=1)
    total_price = Column(Integer)

    customer = relationship('Customer', back_populates='orders')
    laptop = relationship('Laptop', back_populates='orders')

    # def __repr__(self):
    #     return f"<Order(id='{self.id}', customer_id='{self.customer_id}', laptop_id='{self.laptop_id}', quantity='{self.quantity}', total_price='{self.total_price}')>"


Base.metadata.create_all(engine)

   
 