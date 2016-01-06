from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
print 'start app'
db = SQLAlchemy()
def create_app(config_name):
	app = Flask(__name__)
	db.init_app(app)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	return app