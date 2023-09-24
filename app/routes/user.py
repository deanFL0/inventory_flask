from flask import render_template, redirect, url_for, request, Blueprint
from app.models import db, Users

user_bp = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user_bp.route('/')
def index():
    return redirect(url_for('user.userList'))

@user_bp.route('/list', methods=['GET'])
def userList():
    users = Users.query.all()
    for user in users:
        print(user)
    return render_template('/user/index.html', users=users)

@user_bp.route('/add')
def userAdd():
    return render_template('/user/create.html')

@user_bp.route('/save', methods=['POST'])
def userSave():
    user = Users(name=request.form['name'], username=request.form['username'],
                 password=request.form['password'], role=request.form['role'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('user.userList'))

@user_bp.route('/edit/<int:id>')
def userEdit(id):
    user = Users.query.filter_by(id=id).first()
    return render_template('/user/edit.html', user=user)

@user_bp.route('/update', methods=['POST'])
def userUpdate():
    user = Users.query.filter_by(id=request.form['id']).first()
    user.name = request.form['name']
    user.username = request.form['username']
    user.password = request.form['password']
    user.role = request.form['role']
    db.session.commit()
    return redirect(url_for('user.userList'))

@user_bp.route('/delete/<int:id>')
def userDelete(id):
    user = Users.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.userList'))
