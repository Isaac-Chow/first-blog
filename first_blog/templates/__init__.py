from flask import Flask
from first_blog.config import DevelopmentConfig as D
# > Create a class instance from the Flask class
# > The first argument is the name of the application's module or package
# > The second argument is the path to the template folder
# > The third argument is the name of the folder that contains static files
# > The fourth argument is the path to the static folder
# Reference: https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask
app=Flask(
    __name__,
    template_folder="templates",
    static_folder="../static",
    static_url_path="/../static"
)

# Setup the configuration
# Reference: https://flask.palletsprojects.com/en/2.2.x/config/#configuring-from-files

app.config.from_object(D)