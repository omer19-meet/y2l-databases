from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, picture, price , description, stock):
    Product_obj = Product(
        name=name,
        picture=picture,
        price=price,
        description=description,
        stock=stock
        )
    session.add(Product_obj)
    session.commit()

def delete_product(their_name):
	session.query(Product).filter_by(
       name=their_name).delete()
   session.commit()

add_product("ballon", "no", 80, "good", True)
add_product("shoko", "-", 10, "without sugur", False)

# Write your functions to interact with the database here :

# def create_product():
#   #TODO: complete the functions (you will need to change the function's inputs)
#   pass

# def update_product():
#   #TODO: complete the functions (you will need to change the function's inputs)
#   pass

# def delete_product(id):
#   pass

# def get_product(id):
#   pass
