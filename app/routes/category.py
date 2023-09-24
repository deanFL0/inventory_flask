from flask import Blueprint, render_template, redirect, url_for, request
from app.models import db, Categories

category_bp = Blueprint('category', __name__, template_folder='templates', static_folder='static')

@category_bp.route('/')
def index():
    return redirect(url_for('category.categoryList'))

@category_bp.route('/list', methods=['GET'])
def categoryList():
    categories = Categories.query.all()
    return render_template('category/index.html', categories=categories)

@category_bp.route('/add')
def categoryAdd():
    return render_template('category/create.html')

@category_bp.route('/save', methods=['POST'])
def categoryCreate():
    category = Categories(name=request.form['name'], description=request.form['description'])
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('category.categoryList'))

@category_bp.route('/edit/<int:id>', methods=['GET'])
def categoryEdit(id):
    category = Categories.query.filter_by(id=id).first()
    return render_template('category/edit.html', category=category)

@category_bp.route('/update', methods=['POST'])
def categoryUpdate():
    category = Categories.query.filter_by(id=request.form['id']).first()
    category.name = request.form['name']
    category.description = request.form['description']
    db.session.commit()
    return redirect(url_for('category.categoryList'))

@category_bp.route('/delete/<int:id>', methods=['GET'])
def categoryDelete(id):
    category = Categories.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('category.categoryList'))

