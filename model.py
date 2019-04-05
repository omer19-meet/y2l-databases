from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Product(Base):
		__tablename__ = 'Products'
   		id = Column(Integer, primary_key=True)
   		name = Column(String)
   		picture = Column(String)
   		price = Column(Integer)
   		description = Column(String)
   		stock = Column(Boolean)


# def add_product(name, picture, price , description, stock):
#     Product_obj = Product(
#         name=name,
#         picture=picture,
#         price=price,
#         description=description,
#         stock=stock
#         )
#     session.add(student_object)
#     session.commit()

# add_product("ballon", "no", 80, "good", True)




