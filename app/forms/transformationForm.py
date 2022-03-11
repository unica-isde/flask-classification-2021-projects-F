from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import NumberRange, DataRequired
from app.utils.list_images import list_images

class TransformationForm(FlaskForm):

    brightness = FloatField('brightness', validators = [NumberRange(min=0, max=1)])
    saturation = FloatField('saturation', validators = [NumberRange(min=0, max=1)])
    contrast = FloatField('contrast', validators = [NumberRange(min=0, max=1)])
    hue = FloatField('hue', validators = [NumberRange(min=0, max=1)])
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])

    submit = SubmitField('Submit')
