from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

from recommender import champ_names

class ChooseForm(FlaskForm):
    choose_champ = SelectField(u'Campeón: ', validators=[DataRequired()],
    choices=champ_names)
    submit = SubmitField('Mostrar recomendaciones')