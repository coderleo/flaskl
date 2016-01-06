from . import db
print 'start model'
class Entity(db.Model):
	__abstract__  = True
	id = db.Column(db.Integer,primary_key = True)
	created_time = db.Column(db.DateTime,nullable = False,default=db.func.now())
	created_by = db.Column(db.String(10),nullable = True)
	modified_time = db.Column(db.DateTime,default=db.func.now())
	modified_by = db.Column(db.String(10),nullable = True)

class ArticleType(Entity):
	__tablename__ = 'articletypes'
	title = db.Column(db.String(100),nullable = False)
	articles = db.relationship('Article',backref = 'articletype',lazy = 'dynamic')
class Article(Entity):
	__tablename__ = 'articles'
	title = db.Column(db.String(100),nullable = False)
	content = db.Column(db.String(1000))
	type_id = db.Column(db.Integer,db.ForeignKey('articletypes.id'))
class User(Entity):
	__tablename__ = 'users'
	name = db.Column(db.String(10),nullable = False)
	password = db.Column(db.String(100))
class Power(Entity):
	__tablename__ = 'powers'
	name = db.Column(db.String(10),nullable = False)
	description = db.Column(db.String(100))