from flask_sqlalchemy import  SQLAlchemy
from . import app

db=SQLAlchemy(app)

# Create and define a class called User
class User(db.Model):
    # set the id to a primary key
    id = db.Column(db.Integer)
    # column for name
    name=db.Column(db.String)
    # column for email
    email=db.Column(db.String)
    # column for password
    pw=db.Column(db.String)
    # column for phone
    phone=db.Column(db.String)

    # define str method that returns the name of teh user
    def __str__(self)->str:
        return f"Name: {self.name}, Email: {self.email}"


    # define repr method that returns the name of teh user
    def __repr__(self)->str:
        return f"<Name: {self.name}, Password: {self.password} Email: {self.email}>"


    
# Create and define a class called Product
class Product(db.Model):
    def __init__(self, title, price, description, category, rating ):
        super.__init__()
# The product should have the followwing attributes:
# id
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        # title
        title=db.Column(db.String)
        # price
        price=db.Column(db.Integer)
        # description
        desc=db.Column(db.String)
        # category
        category=db.Column(db.String)
        # image
        img=db.Column(db.String)
        # rating
        rating=db.Column(db.Integer)
