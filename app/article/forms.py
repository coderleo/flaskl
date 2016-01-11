from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
#from flask.ext.pagedown.fields import PageDownField

class TypeForm(Form):
	title = StringField(validators=[Required()])
	description = TextAreaField()
	submit = SubmitField()