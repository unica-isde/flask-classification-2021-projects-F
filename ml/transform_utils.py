from ml.classification_utils import fetch_image
from torchvision import transforms
import torchvision.utils
import os,time
from datetime import datetime

from config import Configuration
conf = Configuration()

def transform_image(img_id, brightness_id, contrast_id, saturation_id, hue_id):
    """Returns the image with the corresponding transformations (choosen by the user) applied"""
    
    #fetching the image
    img = fetch_image(img_id)

    try:
        os.mkdir(conf.transformed_folder_path) #we try to create the output folder
    except FileExistsError: #if the folder already exists we remove the previous output files
        for f in os.listdir(conf.transformed_folder_path):
            os.remove(os.path.join(conf.transformed_folder_path, f))

    #creation of the transform object that combines all the transformations that we want to apply to the image
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.ColorJitter(
                brightness_id,
                contrast_id,
                saturation_id,
                hue_id
            )
        ]
    )


    # apply transform from torchvision
    img = img.convert('RGB')
    preprocessed = transform(img)

    img.close()
    
    #retrieving current time to create an unique filename
    now = time.time_ns()
    img_name = str(now) + '.JPEG'
    #saving the image to the ouput folder
    output_path = os.path.join(conf.transformed_folder_path, img_name)
    torchvision.utils.save_image(preprocessed, output_path)

    return img_name
