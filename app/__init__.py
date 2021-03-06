from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
print 'start app'
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection ="strong"
login_manager.login_view = "auth.login"
def create_app(config_name):
	app = Flask(__name__)
	db.init_app(app)
	login_manager.init_app(app)
	bootstrap.init_app(app)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	from .article import article as article_blueprint
	from .auth import auth as auth_blueprint
	
	app.register_blueprint(article_blueprint,url_prefix = '/article')
	app.register_blueprint(auth_blueprint,url_prefix='/auth')
	return app