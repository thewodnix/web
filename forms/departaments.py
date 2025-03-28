from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, \
    IntegerField, EmailField
from wtforms.validators import DataRequired


class DepartamentsForm(FlaskForm):
    title = StringField('Заголовок')
    chief = IntegerField("id")
    members = StringField("Участники")
    email = EmailField("Почта", validators=[DataRequired()])
    submit = SubmitField('Применить')
