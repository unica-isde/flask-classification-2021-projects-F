from config import Configuration
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FileField
from wtforms.validators import DataRequired
from app.utils.list_images import list_images

conf = Configuration()

class UploadForm(FlaskForm):
    '''
    Let the user to choose model and upload image to analyze
    '''
    model = SelectField('model', choices=conf.models, validators=[DataRequired()])
    image = FileField('image', validators=[DataRequired()])
    submit = SubmitField('Submit')
