import os.path
from config import Configuration
from werkzeug.utils import secure_filename


def allowed_image(filename):
    """
    This function returns True or False whether the image is suitable to be uploaded or not
    it returns false when the image has no extension or the extension is not one of the allowed ones
    """
    if "." not in filename:  # no file extension
        return False
    extension = filename.rsplit(".", 1)[1]
    if extension.lower() in Configuration.ALLOWED_EXTENSIONS:
        return True
    else:
        return False


def check_upload(image):
    """
    This function return True when an image was actually uploaded to the form and is allowed for the upload
    False is returned when the form has no image or when the image is not suitable for the upload
    """
    if image.filename == "":
        return False
    if not allowed_image(image.filename):
        return False
    return True


def save_image(image):
    """
    This function is used to actually save the image to the folder
    it also creates the image folder in the case that there is no folder for the uploaded images
    It returns the folder where the image is stored and the secure filename used for the uploaded image
    """
    filename = secure_filename(image.filename)
    img_folder = Configuration.UPLOAD_FOLDER
    if not os.path.exists(img_folder):
        os.mkdir(img_folder)
    image.save(os.path.join(img_folder, filename))
    image.close()
    return filename, img_folder
