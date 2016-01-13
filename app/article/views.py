from flask import render_template, redirect,url_for,abort,flash,request
from . import article
from .forms import TypeForm, ArticleForm
from ..models import ArticleType,Article
from datetime import datetime
from .. import db
from sqlalchemy.orm import joinedload,subqueryload
@article.route('/')
def index():
	list =Article.query.options(joinedload('articletype').joinedload('test')).all()
	return render_template('article_list.html',list = list)
@article.route('/create',methods=['GET','POST'])
def create():
	form = ArticleForm()
	print form.validate_on_submit()
	if form.validate_on_submit():
		article = Article(title = form.title.data,content = form.content.data,type_id = form.article_type.data)
		db.session.add(article)
		db.session.commit()
		return redirect(url_for('.index'))
		#print form.data
	return render_template('create.html',form = form)
@article.route('/type/create',methods=['GET','POST'])
def create_type():
	form = TypeForm()
 
	if form.validate_on_submit():
		print form.title.data
		type = ArticleType(title=form.title.data,description = form.description.data,modified_time=datetime.now())
		print 'bbb'
		db.session.add(type)
		db.session.commit()
		print url_for('.index_type')
		return redirect(url_for('.index_type'))
	print 'bbb'
	return render_template('create_type.html',form = form)
@article.route('/type')
def index_type():
	list = ArticleType.query.all()
	return render_template('type_list.html',list = list)


