from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
from recommender import CHAMP_NAMES


NUM_CHOICES = [(1.0, "Bajo"), (2.0, "Medio"), (3.0, "Alto")]
LANE_CHOICES = ["Top", "Mid", "Bottom", "Jungle", "Support"]
DTYPE_CHOICES = [("DType_Magic", "Magic"), ("DType_Physical", "Physical")]
ROL_CHOICES = [
    ("Rol_Artillery", "Artillery"), 
    ("Rol_Assassin", "Assassin"), 
    ("Rol_Battlemage", "Battlemage"), 
    ("Rol_Burst", "Burst"), 
    ("Rol_Catcher", "Catcher"), 
    ("Rol_Diver", "Diver"), 
    ("Rol_Enchanter", "Enchanter"),
    ("Rol_Juggernaut", "Juggernaut"), 
    ("Rol_Marksman", "Marksman"), 
    ("Rol_Skirmisher", "Skirmisher"), 
    ("Rol_Specialist", "Specialist"), 
    ("Rol_Vanguard", "Vanguard"), 
    ("Rol_Warden", "Warden")
]


class ChooseForm(FlaskForm):
    choose_champ = SelectField(u"Campeón", choices=CHAMP_NAMES)
    submit = SubmitField("Mostrar recomendaciones")

class StatForm(FlaskForm):
    rol = SelectField(u"Rol", choices=ROL_CHOICES)
    linea = SelectField(u"Lane", choices=LANE_CHOICES)
    tipo = SelectField(u"Damage Type", choices=DTYPE_CHOICES)
    damage = SelectField(u"Damage", choices=NUM_CHOICES, default=2.0)
    toughness = SelectField(u"Toughness", choices=NUM_CHOICES, default=2.0)
    control = SelectField(u"Control", choices=NUM_CHOICES, default=2.0)
    mobility = SelectField(u"Mobility", choices=NUM_CHOICES, default=2.0)
    utility = SelectField(u"Utility", choices=NUM_CHOICES, default=2.0)
    difficulty = SelectField(u"Difficulty", choices=NUM_CHOICES, default=2.0)
    submit_stat = SubmitField("Mostrar recomendaciones")
