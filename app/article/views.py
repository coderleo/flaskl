from flask import render_template, redirect,url_for,abort,flash,request
from . import article
from .forms import TypeForm
from ..models import ArticleType
from datetime import datetime
from .. import db
@article.route('/')
def index():
	abort(500)

@article.route('/type/create',methods=['GET','POST'])
def create_type():
	form = TypeForm()
	print form.errors
	if form.validate_on_submit():
		print 'ccc'
		type = ArticleType(title=form.data.title,description = form.data.description,modified_time=datetime.now())
		print 'bbb'
		db.session.add(type)
		db.session.commit()
	print 'bbb'
	return render_template('create_type.html',form = form)