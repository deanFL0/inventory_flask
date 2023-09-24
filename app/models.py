from sqlalchemy import Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Items(db.Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)
    description = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    rack_id = Column(Integer, ForeignKey('rack.id'))

    def __repr__(self):
        return "<Items(name='%s', price='%s', quantity='%s', description='%s', category_id='%s', rack_id='%s')>" % (self.name, self.price, self.quantity, self.description, self.category_id, self.rack_id)

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    username = Column(String(255))
    password = Column(String(255))
    role = Column(String(255))

    def __repr__(self):
        return "<Users(username='%s', password='%s', role='%s')>" % (self.username, self.password, self.role)
    
class Categories(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    items = db.relationship('Items', backref='categories', lazy=True)

    def __repr__(self):
        return "<Categories(name='%s', description='%s')>" % (self.name, self.description)
    
class Rack(db.Model):
    __tablename__ = 'rack'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    items = db.relationship('Items', backref='rack', lazy=True)

    def __repr__(self):
        return "<Rack(name='%s', description='%s')>" % (self.name, self.description)
