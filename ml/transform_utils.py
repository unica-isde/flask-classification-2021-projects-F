from ml.classification_utils import fetch_image
from torchvision import transforms
import torchvision.utils
import os,time
from datetime import datetime

from config import Configuration
conf = Configuration()

def transform_image(img_id, brightness_id, contrast_id, saturation_id, hue_id):
    """Returns the top-5 classification score output from the
    model specified in model_id when it is fed with the
    image corresponding to img_id."""
    img = fetch_image(img_id)

    try:
        os.mkdir(conf.transformed_folder_path)
    except FileExistsError:
        for f in os.listdir(conf.transformed_folder_path):
            os.remove(os.path.join(conf.transformed_folder_path, f))

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

    now = time.time_ns()
    img_name = str(now) + '.JPEG'
    output_path = os.path.join(conf.transformed_folder_path, img_name)
    torchvision.utils.save_image(preprocessed, output_path)

    return img_name