from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import NumberRange, DataRequired
from app.utils.list_images import list_images

class TransformationForm(FlaskForm):
    '''
    Let the user pick the value of brightness, saturation, contrast, hue and the image for transformation form
    '''
    brightness = FloatField('brightness', validators = [NumberRange(min=0, max=1)], default=0)
    saturation = FloatField('saturation', validators = [NumberRange(min=0, max=1)], default=0)
    contrast = FloatField('contrast', validators = [NumberRange(min=0, max=1)], default=0)
    hue = FloatField('hue', validators = [NumberRange(min=0, max=1)], default=0)
    image = SelectField('image', choices=list_images(), validators=[DataRequired()])

    submit = SubmitField('Submit')
