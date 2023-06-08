from first_blog import app
from flask import render_template, request, redirect, url_for, flash
import json
from .models import db, Product, User, Order, create_db, add_data
from .forms import UserRegForm, ProductForm, SearchForm, LoginForm
from first_blog.products import data

# Since we are using SQLAlchemy, we can query the database for the data
# use app.app_context() to access the app since the db is not in the same file
# Reference: https://flask.palletsprojects.com/en/2.0.x/appcontext/#manually-push-a-context
with app.app_context():
    # create the database
    create_db()
    # add the data to the database
    add_data()
    # query the database for the data
    dataItems = Product.query.all()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Product=Product, data=dataItems, Order=Order)


@app.shell_context_processor
def make_shell_context():
    return {"app": app, "db": db, "User": User, "Product": Product, "Order": Order}


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    global dataItems
    return render_template(
        "index.html",
        data=dataItems
    )


@app.route("/about")
def about():
    return render_template(
        "about.html"
    )


@app.route("/article")
def article():
    return render_template(
        "article.html"
    )

# Create a path for /products/<str>
# define a function called  product


@app.route("/products/<int:id>")
def product(id):
    # Access the item passed from the dictionary
    product_py = dict()

    for item in dataItems:
        if item['id'] == id:
            product_py = item

    return render_template(
        "product.html",
        product_jinja=product_py
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        register = UserRegForm()
        return render_template(
            "register.html",
            register=register
        )
    if request.method == "POST":
        pass


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        login: LoginForm = LoginForm()

        return render_template(
            "login.html",
            login=login
        )
    if request.method == "POST":
        pass


@app.route("/logout")
def logout():
    # redirect to the login page
    return redirect(url_for("login"))


@app.route("/addproduct/", methods=["GET", "POST"])
def addproduct():
    if request.method == "GET":
        addproduct: ProductForm = ProductForm()
        searchproduct: SearchForm = SearchForm()
        return render_template(
            "addproduct.html",
            addproduct=addproduct,
            searchproduct=searchproduct
        )
    if request.method == "POST":
        addproduct: ProductForm = ProductForm()
        searchproduct: SearchForm = SearchForm()
        # validate the form and get the data
        # create a new product object
        # add the product to the database
        # commit the changes
        ############### START HERE ################
        if addproduct.validate():
            product = Product(
                title=addproduct.title.data,
                price=addproduct.price.data,
                desc=addproduct.desc.data,
                category=addproduct.category.data,
                img=addproduct.img.data,
            )
            # rating=0
            with app.app_context():
                db.session.add(product)
                db.session.commit()
                global dataItems
                dataItems = Product.query.all()

            return redirect(url_for("added_successfully"))
        else:
            return redirect(url_for("failed_add"))

        ############### END HERE ################


@app.route("/added_successfully")
def added_successfully():
    return render_template(
        "added_successfully.html"
    )


@app.route("/failed_add")
def failed_add():
    return render_template(
        "failed_add.html"
    )
