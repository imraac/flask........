from flask import Flask
from flask_migrate import Migrate
from models import db
app = Flask (__name__)

# configuration data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'



# migrate
migrate = Migrate(app, db)

# initialize SQLAlchemy
db.init_app(app)

# base/index/root route
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "Contact Page"

@app.route("/contact/<username_id>")
def contact_id(username_id):
    return f"Contact Page for {username_id}"
