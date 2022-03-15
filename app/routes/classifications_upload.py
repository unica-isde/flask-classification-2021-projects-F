from flask import request, render_template, redirect
from app import app
from app.forms.classification_form import ClassificationForm
from ..utils.image_upload import check_upload, save_image


@app.route('/classifications_upload', methods=['GET', 'POST'])
def classifications_upload():
    form = ClassificationForm()
    if request.method == "POST":
        # check if the form has the image field
        if 'uploaded_img' not in request.files:
            return redirect(request.url)
        image = request.files['uploaded_img']
        if not check_upload(image):
            return redirect(request.url)
        # saving the image
        filename, img_folder = save_image(image)


    return render_template('classifications_upload.html', form=form)
