# For flask_wtf, the "wtf" in the name doesn't mean what you think. It means WSGITemplateForms. On the other hand, "WIGI" means ?
from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField,IntegerField
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
    name=StringField("Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired()])
    password=StringField("Password",validators=[DataRequired()])
    recaptcha=RecaptchaField()

    def __repr__(self):
        return f"UserRegaform({self.name},{self.email},{self.password})"
    
    def validate(self):
        if not super().validate():
            return False
        
        user= User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True