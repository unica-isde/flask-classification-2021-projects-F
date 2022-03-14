from flask import request, render_template
from app import app
from app.forms.classification_form import ClassificationForm


@app.route('/classifications_upload', methods=['GET', 'POST'])
def classifications_upload():
    
    form = ClassificationForm()
    if request.method == "POST":
       # TODO  
       pass

    return render_template('classifications_upload.html', form=form)