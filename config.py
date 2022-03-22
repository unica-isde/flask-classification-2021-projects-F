import os

project_root = os.path.dirname(os.path.abspath(__file__))


class Configuration:
    """Contains the configuration information for the app."""

    # file upload
    UPLOAD_FOLDER = os.path.join(project_root, 'app/static/imagenet_subset')
    ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png', 'webp', 'gif'}
    # classification
    image_folder_path = os.path.join(project_root, 'app/static/imagenet_subset')
    transformed_folder_path = os.path.join(project_root, 'app/static/transformed_image')
    models = ('resnet18', 'alexnet', 'vgg16', 'inception_v3',)
    # web server
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9cj328s61hsd8'
    # queue
    REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    QUEUE = "classification"
