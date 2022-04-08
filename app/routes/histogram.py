import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.histogram_form import HistogramForm
from ..utils.histogram_plot import make_histogram_plot
from config import Configuration

config = Configuration()


@app.route('/histogram', methods=['GET', 'POST'])
def histogram():
    '''
    API for calculating the histogram of a selected image
    '''
    form = HistogramForm()
    if form.validate_on_submit():  # POST
        image_id = form.image.data
        plot = make_histogram_plot(image_id)  # histogram html/js code
        return render_template('histogram_result.html', plot=plot, image_id=image_id)

    # otherwise, it is a get request and should return the image selector
    return render_template('histogram_select.html', form=form)
