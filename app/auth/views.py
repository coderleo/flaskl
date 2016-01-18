from . import auth
from flask import render_template,redirect,url_for,abort,flash,request

from .forms import RegistrationForm
from .. import db 
from ..models import User
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