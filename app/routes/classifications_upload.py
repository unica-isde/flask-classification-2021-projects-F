from flask import request, render_template, redirect
from app import app
from app.forms.upload_form import UploadForm
from ..utils.image_upload import check_upload, save_image
from ml.classification_utils import classify_image
from config import Configuration
import redis
from rq import Connection, Queue
from rq.job import Job

config = Configuration()

@app.route('/classifications_upload', methods=['GET', 'POST'])
def classifications_upload():
    '''
    This function save the uploaded image, start the classification job and returns the classification results in a rendered page
    '''
    form = UploadForm()

    if request.method == "POST":
        # check if the form has the image field
        if 'image' not in request.files:
            return redirect(request.url)
        image = request.files['image']
        if not check_upload(image):
            return redirect(request.url)
        # saving the image
        filename, img_folder = save_image(image)

        image_id = form.image.data.filename
        model_id = form.model.data

        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            job = Job.create(classify_image, kwargs={
                "model_id": model_id,
                "img_id": image_id
            })
            task = q.enqueue_job(job)

        return render_template("classification_output_queue.html", image_id=image_id, jobID=task.get_id())

    return render_template('classifications_upload.html', form=form)
