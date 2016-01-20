from . import db,login_manager
from werkzeug.security import check_password_hash,generate_password_hash
from flask.ext.login import UserMixin,AnonymousUserMixin
class Entity(db.Model):
	__abstract__  = True
	id = db.Column(db.Integer,primary_key = True)
	created_time = db.Column(db.DateTime,nullable = False,default=db.func.now())
	created_by = db.Column(db.String(10),nullable = True)
	modified_time = db.Column(db.DateTime,nullable = True)
	modified_by = db.Column(db.String(10),nullable = True)

class ArticleType(Entity):
	__tablename__ = 'articletypes'
	title = db.Column(db.String(100),nullable = False)
	description = db.Column(db.String(1000))
	articles = db.relationship('Article',backref = 'articletype',lazy = 'dynamic')
	test_id = db.Column(db.Integer,db.ForeignKey('tests.id'))
class Article(Entity):
	__tablename__ = 'articles'
	title = db.Column(db.String(100),nullable = False)
	content = db.Column(db.String(1000))
	read_count = db.Column(db.Integer)
	publish_time = db.Column(db.DateTime,nullable=True)
	type_id = db.Column(db.Integer,db.ForeignKey('articletypes.id'))
	
users_powers = db.Table('users_powers',db.Column('power_id',db.Integer,db.ForeignKey('powers.id'),nullable=False),db.Column('user_id',db.Integer,db.ForeignKey('users.id'),nullable=False))
class User(UserMixin,Entity):
	__tablename__ = 'users'
	name = db.Column(db.String(10),nullable = False)
	password_hash = db.Column(db.String(128))
	powers = db.relationship('Power',secondary = users_powers,backref='users')
	email = db.Column(db.String(128))
	@property
	def password(self):
		raise AttributeError("password is not readable attribute")
	@password.setter 
	def password(self,pwd):
		self.password_hash = generate_password_hash(pwd)
	def validate_user(self,pwd):
		return check_password_hash(self.password_hash, pwd)
class Power(Entity):
	__tablename__ = 'powers'
	name = db.Column(db.String(10),nullable = False)
	description = db.Column(db.String(100))
class Action(Entity):
	__tablename__ = 'actions'
	name = db.Column(db.String(10),nullable = False)
	module_id = db.Column(db.String(10),nullable= False)
	order = db.Column(db.Integer)
class Test(Entity):
	__tablename__ = 'tests'
	title = db.Column(db.String(10))
	types = db.relationship('ArticleType',backref = 'test',lazy = 'dynamic')
class AnonymousUser(AnonymousUserMixin):
	def can(self, permissions):
		return False

	def is_administrator(self):
	    return False

login_manager.anonymous_user = AnonymousUser
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))