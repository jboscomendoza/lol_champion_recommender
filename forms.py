from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
from recommender import CHAMP_NAMES


NUM_CHOICES = [(1.0, "Bajo"), (2.0, "Medio"), (3.0, "Alto")]
LANE_CHOICES = [(1, "Top"), (2, "Jungle"), (3, "Mid"), (4, "Bottom"), (5, "Support")]
ROL_CHOICES = [
    "Artillery", "Assassin", "Battlemage", "Burst", "Catcher", "Diver", "Enchanter",
    "Juggernaut", "Marksman", "Skirmisher", "Specialist", "Vanguard", "Warden"
]


class ChooseForm(FlaskForm):
    choose_champ = SelectField(u"Campeón: ", validators=[DataRequired()],
    choices=CHAMP_NAMES)
    submit = SubmitField("Mostrar recomendaciones")

class StatForm(FlaskForm):
    rol = SelectField(u"Rol", choices=ROL_CHOICES)
    lane = SelectField(u"Lane", choices=LANE_CHOICES)
    damage = SelectField(u"Damage", choices=NUM_CHOICES)
    toughness = SelectField(u"Toughness", choices=NUM_CHOICES)
    control = SelectField(u"Control", choices=NUM_CHOICES)
    mobility = SelectField(u"Mobility", choices=NUM_CHOICES)
    utility = SelectField(u"Utility", choices=NUM_CHOICES)
    difficulty = SelectField(u"Difficulty", choices=NUM_CHOICES)
    
    submit = SubmitField("Mostrar recomendaciones")
