from flask import render_template, redirect, url_for, request, Blueprint
from app.models import db, Items, Categories, Rack

item_bp = Blueprint('item', __name__, template_folder='templates', static_folder='static')

#routes
@item_bp.route('/')
def index():
    return redirect(url_for('item.itemList'))

@item_bp.route('/list', methods=['GET'])
def itemList():
    items = Items.query.all()
    categories = Categories.query.all()
    rack = Rack.query.all()
    for item in items:
        print(item)
    return render_template('/item/index.html', items=items, categories=categories, rack=rack)

@item_bp.route('/add')
def itemAdd():
    categories = Categories.query.all()
    rack = Rack.query.all()
    return render_template('/item/create.html', categories=categories, racks=rack)

@item_bp.route('/save', methods=['POST'])
def itemSave():
    item = Items(name=request.form['name'], 
                 price=request.form['price'], 
                 quantity=request.form['quantity'], 
                 description=request.form['description'],
                 category_id=request.form['category'],
                 rack_id=request.form['rack'])
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('item.itemList'))

@item_bp.route('/edit/<int:id>')
def itemEdit(id):
    item = Items.query.filter_by(id=id).first()
    categories = Categories.query.all()
    rack = Rack.query.all()
    return render_template('/item/edit.html', item=item, categories=categories, racks=rack)

@item_bp.route('/update', methods=['POST'])
def itemUpdate():
    item = Items.query.filter_by(id=request.form['id']).first()
    rack = Rack.query.filter_by(id=request.form['rack']).first()
    category = Categories.query.filter_by(id=request.form['category']).first()
    item.name = request.form['name']
    item.price = request.form['price']
    item.quantity = request.form['quantity']
    item.description = request.form['description']
    item.rack_id = request.form['rack']
    item.category_id = request.form['category']
    db.session.commit()
    return redirect(url_for('item.itemList'))

@item_bp.route('/delete/<int:id>')
def itemDelete(id):
    item = Items.query.filter_by(id=id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('item.itemList'))