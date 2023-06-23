from flask_sqlalchemy import SQLAlchemy
from . import app
from .products import data
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy(app)



# Create and define a class called User
class User(db.Model):
    # set the id to a primary key
    id = db.Column(db.Integer, primary_key=True)
    # column for name
    name = db.Column(db.String, nullable=False)
    # column for email
    email = db.Column(db.String, nullable=False)
    # column for password
    pw = db.Column(db.String, nullable=False)
    # column for phone
    phone = db.Column(db.String, nullable=False)


    # define str method that returns the name of teh user
    def __str__(self) -> str:
        return f"Name: {self.name}, Email: {self.email}"

    # define repr method that returns the name of teh user
    def __repr__(self) -> str:
        return f"<Name: {self.name}, Password: {self.password} Email: {self.email}>"

    @property
    def password(self):
        return "You can't access the password"
    
    def set_password(self,password):
        self.pw=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pw,password)
    
# Create and define a class called Product
class Product(db.Model):
    # def __init__(self, title, price, description, category, rating ):
    #     super.__init__()
    # The product should have the followwing attributes:
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # title
    title = db.Column(db.String, nullable=False)
    # price
    price = db.Column(db.Integer, nullable=False)
    # description
    desc = db.Column(db.String, nullable=False)
    # category
    category = db.Column(db.String, nullable=False)
    # image
    img = db.Column(db.String, nullable=False)
    # rating
    rating = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Product({self.title} {self.price} {self.category})>"


class Order(db.Model):

    # link the order to a specific user using a foreign key
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )

    # Create a relationship between order and user
    user = db.relationship(
        "User", backref=db.backref("order", lazy=True)
    )

    # link the order to a specific user using a foreign key
    product_id = db.Column(
        db.Integer, db.ForeignKey("product.id"), nullable=False
    )

    # Create a relationship between order and user
    product = db.relationship(
        "Product", backref=db.backref("order", lazy=True)
    )

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<Product({self.user}, {self.product})>"




# Create a function that will create the database
def create_db():
    # drop all existing tables
    db.drop_all()
    # create all tables
    db.create_all()
    # commit changes
    db.session.commit()
    print("***************************************")
    print("**   Confirmed: Database Created  *****")
    print("***************************************")

# Read from the json file and add the data to the database
def add_data():
    for i in range(len(data)):
        db_prod_item = Product(
            id=data[i]["id"], title=data[i]["title"],
            price=data[i]["price"], desc=data[i]["description"],
            category=data[i]["category"], img=data[i]["image"], 
            rating=data[i]["rating"]["rate"]
        )
        db.session.add(db_prod_item)
        db.session.commit()

    print("*********************************************")
    print("**   Confirmed: Data Added to Database  *****")
    print("*********************************************")