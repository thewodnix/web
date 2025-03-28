from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, \
    IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Заголовок')
    team_leader = IntegerField("id тимлида")
    work_size = IntegerField("Время работы")
    collaborators = StringField("Колабораторы")
    is_finished = SubmitField('Готово?')
    submit = SubmitField('Применить')
