from . import db
print 'start model'
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
	
class Article(Entity):
	__tablename__ = 'articles'
	title = db.Column(db.String(100),nullable = False)
	content = db.Column(db.String(1000))
	read_count = db.Column(db.Integer)
	publish_time = db.Column(db.DateTime,nullable=True)
	type_id = db.Column(db.Integer,db.ForeignKey('articletypes.id'))
	
users_powers = db.Table('users_powers',db.Column('power_id',db.Integer,db.ForeignKey('powers.id'),nullable=False),db.Column('user_id',db.Integer,db.ForeignKey('users.id'),nullable=False))
class User(Entity):
	__tablename__ = 'users'
	name = db.Column(db.String(10),nullable = False)
	password = db.Column(db.String(100))
	powers = db.relationship('Power',secondary = users_powers,backref='users')
class Power(Entity):
	__tablename__ = 'powers'
	name = db.Column(db.String(10),nullable = False)
	description = db.Column(db.String(100))
class Action(Entity):
	__tablename__ = 'actions'
	name = db.Column(db.String(10),nullable = False)
	module_id = db.Column(db.String(10),nullable= False)
	order = db.Column(db.Integer)