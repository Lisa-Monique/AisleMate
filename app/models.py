from app import db, bcrypt
import flask_login

class User(db.Model, flask_login.UserMixin):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(128))
	lists = db.relationship('List', backref='author', lazy='dynamic')
	

	def is_correct_password(self, plaintext):
		return bcrypt.check_password_hash(self._password, plaintext)
	
	def __init__(self, email, password):
		self.email = email
		self.password = bcrypt.generate_password_hash(password)
	def __repr__(self):
		return '<User %r>' % (self.email)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	aisle_id = db.Column(db.Integer, db.ForeignKey('aisle.id'))
	list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

class Aisle(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	items = db.relationship('Item', backref='aisle', lazy='dynamic')

	def __repr__(self):
		return '<Items %r>'% (self.items)

class List(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	items = db.relationship('Item', backref='owner', lazy='dynamic')

	def __repr__(self):
		return '<Aisles %r>'% (self.aisles)