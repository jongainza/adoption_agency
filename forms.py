from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField, BooleanField
from wtforms.validators import InputRequired, URL, NumberRange, Optional


class CreateAddForm(FlaskForm):
    name = StringField(
        "Pet Name", validators=[InputRequired(message="Name can not be empty")]
    )
    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo = URLField("Photo", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = StringField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    photo = URLField("Photo", validators=[Optional(), URL()])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Availability", default=True)
