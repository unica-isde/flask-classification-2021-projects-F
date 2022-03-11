from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired


from app.utils.list_images import list_images
from config import Configuration

conf = Configuration()


class ClassificationForm(FlaskForm):
    model = SelectField('model', choices=conf.models, validators=[DataRequired()])
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])
    brightness = FloatField('brightness')
    saturation = FloatField('saturation')
    contrast = FloatField('contrast')
    hue = FloatField('hue')

    submit = SubmitField('Submit')
