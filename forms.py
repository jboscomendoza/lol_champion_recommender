from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

from recommender import CHAMP_NAMES

class ChooseForm(FlaskForm):
    choose_champ = SelectField(u'Campeón: ', validators=[DataRequired()],
    choices=CHAMP_NAMES)
    submit = SubmitField('Mostrar recomendaciones')