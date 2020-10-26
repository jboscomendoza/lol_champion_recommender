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
    choose_champ = SelectField(u"Campeón", choices=CHAMP_NAMES)
    submit = SubmitField("Mostrar recomendaciones")

class StatForm(FlaskForm):
    role = SelectField(u"Rol", choices=ROL_CHOICES)
    lane = SelectField(u"Lane", choices=LANE_CHOICES)
    dmge = SelectField(u"Damage", choices=NUM_CHOICES)
    tghn = SelectField(u"Toughness", choices=NUM_CHOICES)
    ctrl = SelectField(u"Control", choices=NUM_CHOICES)
    mobl = SelectField(u"Mobility", choices=NUM_CHOICES)
    util = SelectField(u"Utility", choices=NUM_CHOICES)
    diff = SelectField(u"Difficulty", choices=NUM_CHOICES)
    submit_stat = SubmitField("Mostrar recomendaciones")
