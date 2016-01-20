from . import auth
from flask import render_template,redirect,url_for,abort,flash,request
from .forms import RegistrationForm,LoginForm
from .. import db 
from ..models import User
from flask.ext.login import login_user
@auth.route('/register',methods = ['POST','GET'])
def register():
	form = RegistrationForm()
	print form.errors
	if form.validate_on_submit():
		print form.data
		user = User(name=form.username.data,password=form.pwd.data,email=form.email.data)
		db.session.add(user)
		db.session.commit()
	return render_template('auth/register.html',form = form)
@auth.route('/login',methods=['POST','GET'])
def login():
	form = LoginForm()
	print form.data
	print form.validate_on_submit()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.username.data).first()
		if user is not None and user.validate_user(form.pwd.data):
			login_user(user)
			return redirect(request.args.get('next') or url_for('article.index'))
	return render_template('auth/login.html',form=form)