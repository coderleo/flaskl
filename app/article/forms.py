from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import ArticleType
#from flask.ext.pagedown.fields import PageDownField

class TypeForm(Form):
	title = StringField(validators=[Required()])
	description = TextAreaField()
	submit = SubmitField()
class ArticleForm(Form):
	title = StringField(validators=[Required()])
	content = TextAreaField(validators=[Required()])
	article_type = SelectField('article_type',coerce=int)
	submit = SubmitField()
	def __init__(self,*args,**kwargs):
		super(ArticleForm, self).__init__(*args,**kwargs)
		self.article_type.choices=[(a_type.id,a_type.title) for a_type in ArticleType.query.all()]