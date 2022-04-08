import numpy as np
import matplotlib.pyplot as plt
import mpld3
from ml.classification_utils import fetch_image


def make_histogram_plot(image_id):
    """
    This function returns the html and js code for the histogram plot of an image, given its id.
    """
    img_array = fetch_image(image_id)
    img_array = np.array(img_array.convert('RGB'))

    # calculate mean value from RGB channels and flatten to 1D array
    vals = img_array.mean(axis=2).flatten()

    # assign labels
    plt.xlabel('pixel value')
    plt.ylabel('occurrences')

    # assign title
    plt.title("Histogram of the image")

    plt.plot()

    counts, bins = np.histogram(vals, range(257))
    # plot histogram centered on values 0..255
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    html = mpld3.fig_to_html(
        plt.gcf())  # this function returns the js code that represents the current figure that is handled by matplotlib
    plt.close(plt.gcf())
    return html
