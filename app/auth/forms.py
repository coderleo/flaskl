from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class RegistrationForm(Form):
	username = StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'user name is validate')])
	email = StringField('email',validators=[Required(),Length(1,64),Email()])
	#email2 = PasswordField('email2',validators=[Required(),Length(1,64),Email()])
	pwd = PasswordField('password',validators=[Required(),EqualTo('pwd2',message='Passwords must match.')])
	pwd2 = PasswordField('Confirm password',validators=[Required()])
	submit = SubmitField('Register')
