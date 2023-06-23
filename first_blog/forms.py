# For flask_wtf, the "wtf" in the name doesn't mean what you think. It means WSGITemplateForms. On the other hand, "WIGI" means ?
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from .models import User, Product

"""
To Note:
    > Without any CSRF configuration FlaskForm will secure the forms
    with csrf protection. (Recommended not to change this).
    > Have all your form classes inherit from FlaskForm

    > The default csrt secret key used is same as that of the application,
    but to set up a new one, place a global in your config:
    WTF_CSRF_SECRET_KEY = 'a random string'

"""

class UserRegForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Register")

    def __repr__(self):
        return f"UserRegaform({self.name},{self.email},{self.password})"

    def validate(self):
        if not super().validate():
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


# TODO:
# 1. Create a class called ProductForm that inherits from FlaskForm
# Reference (creating a form class): https://flask.palletsprojects.com/en/2.0.x/patterns/wtforms/#creating-forms)
#
# 2. Add the following fields to the form including the datarequired validator:
#       - title (StringField), validators=[DataRequired()]
#       - price (IntegerField), validators=[DataRequired()]
#       - desc (TextAreaField), validators=[DataRequired()]
#       - category (StringField), validators=[DataRequired()]
#       - img (StringField), validators=[DataRequired()]
#       - rating (IntegerField), validators=[DataRequired()]
#       - recaptcha (RecaptchaField)
#       - submit (SubmitField)
# Reference (wtforms fields): https://wtforms.readthedocs.io/en/2.3.x/fields/
# Reference (wtforms validators): https://wtforms.readthedocs.io/en/2.3.x/validators/
# Reference (wtforms recaptcha): https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.RecaptchaField
# Reference (wtforms submit): https://wtforms.readthedocs.io/en/2.3.x/fields/#wtforms.fields.SubmitField
#
# 3. Add a __repr__ method that returns the following:
#       return f"ProductForm({self.title},{self.price},{self.desc},{self.category},{self.img},{self.rating})"
#
class ProductForm(FlaskForm):
    #################### YOUR CODE STARTS HERE ##################
    title = StringField("Title",validators=[DataRequired()]);
    price = IntegerField("Price",validators=[DataRequired()])
    desc = TextAreaField("Description",validators=[DataRequired()])
    category = StringField("Category",validators=[DataRequired()])
    img = StringField("Image URL",validators=[DataRequired()])
    rating = IntegerField("Rating",validators=[DataRequired()])
    recaptcha = RecaptchaField("Recaptcha")
    submit = SubmitField("Confirm deatails and publish product")

    def __repr__(self):
        return f"ProductForm({self.title},{self.price},{self.desc},{self.category},{self.img},{self.rating})"
    #################### YOUR CODE ENDS HERE ####################

    def validate(self):
        # if not super().validate():
        #     return False

        product = Product.query.filter_by(title=self.title.data).first()
        if product:
            self.title.errors.append("Product already exists")
            return False
        return True


class SearchForm(FlaskForm):
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")

    def __repr__(self):
        return f"SearchForm({self.search})"


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Login")

    def __repr__(self):
        return f"LoginForm({self.email},{self.password})"
