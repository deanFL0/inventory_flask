from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Rack

rack_bp = Blueprint('rack', __name__, template_folder='templates')

@rack_bp.route('/')
def rackIndex():
    return redirect(url_for('rack.rackList'))

@rack_bp.route('/list')
def rackList():
    racks = Rack.query.all()
    return render_template('rack/index.html', racks=racks)

@rack_bp.route('/add')
def rackAdd():
    return render_template('rack/create.html')

@rack_bp.route('/save', methods=['POST'])
def rackSave():
    rack = Rack(name=request.form['name'], description=request.form['description'])
    db.session.add(rack)
    db.session.commit()
    return redirect(url_for('rack.rackList'))

@rack_bp.route('/edit/<int:id>')
def rackEdit(id):
    rack = Rack.query.filter_by(id=id).first()
    return render_template('rack/edit.html', rack=rack)

@rack_bp.route('/update', methods=['POST'])
def rackUpdate():
    rack = Rack.query.filter_by(id=request.form['id']).first()
    rack.name = request.form['name']
    rack.description = request.form['description']
    db.session.commit()
    return redirect(url_for('rack.rackList'))

@rack_bp.route('/delete/<int:id>')
def rackDelete(id):
    rack = Rack.query.filter_by(id=id).first()
    db.session.delete(rack)
    db.session.commit()
    return redirect(url_for('rack.rackList'))
