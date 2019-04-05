from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
# cdcwdwdsdcdscsdcsdcsdcsdcsdcsdcdcsdcdcsdcsdcsdcsdcdcsdcsdccscsdcsdc

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

def delete_product(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()
    # pass

# add_product("ballon", "no", 80, "good", True)
# add_product("cups", "-", 27, "Termic glass", True )
# add_product("shoko", "-", 10, "without sugur", False)

# Write your functions to interact with the database here :

def update_product(id, stock, price):
    prod_obj = session.query(Product).filter_by(id=id).first()
    prod_obj.stock = stock
    prod_obj.price = price
    session.commit()

def first_prod():
    first_p = session.query(Product).first()
    return first_p

# delete_product(7)
print("working")
# def get_product(id):
#   pass
