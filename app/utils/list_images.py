import os

from config import Configuration

conf = Configuration()


def list_images():
    """
    Returns the list of available acceptable images.
    """
    img_names = filter(lambda x: x.endswith('.JPEG'),
                       os.listdir(conf.image_folder_path))
    return list(img_names)
