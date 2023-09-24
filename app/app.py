from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

# Import the Items model
from .models import db
db.init_app(app)

# Import the routes
from .routes.item import item_bp
from .routes.user import user_bp
from .routes.category import category_bp
from .routes.rack import rack_bp
app.register_blueprint(item_bp, url_prefix='/item')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(category_bp, url_prefix='/category')
app.register_blueprint(rack_bp, url_prefix='/rack')

@app.route('/')
def index():
    return redirect(url_for('item.itemList'))