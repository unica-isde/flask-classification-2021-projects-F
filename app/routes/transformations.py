from app.forms.transformationForm import TransformationForm
import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job
from app import app
from ml.classification_utils import classify_image
from ml.transform_utils import transform_image
from config import Configuration
config = Configuration()

@app.route('/transformations', methods=['GET', 'POST'])
def transformations():
    '''
    API for selecting a model and an image and running a
    classification job. Returns the output scores from the
    model.
    '''
    image_name = "trans_image"
    form = TransformationForm()
    if form.validate_on_submit():  # POST

        image_id = form.image.data
        brightness_id = form.brightness.data
        saturation_id = form.saturation.data
        contrast_id = form.contrast.data
        hue_id = form.hue.data

        img_path = transform_image(image_id, brightness_id, contrast_id, saturation_id, hue_id)

        # returns the image classification output from the specified model
        # return render_template('classification_output.html', image_id=image_id, results=result_dict)
        return render_template("transform_output.html", img_path=img_path)

    # otherwise, it is a get request
    return render_template('transform_select.html', form=form)
