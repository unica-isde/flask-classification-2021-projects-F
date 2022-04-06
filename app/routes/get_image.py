from io import BytesIO
from flask import Response
from app import app
from app.utils.result_from_job_id import result_from_job_id
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def bar_chart(numbers, labels):
    '''
    Utility function to create a plot from a given dataset
    '''
    fig,ax=plt.subplots()
    
    colors = ['#6610f2', '#007bff', '#fd7e14', '#dc3545', '#28a745']
    
    ax.barh(labels, numbers, align='center', color=colors)
    plt.legend(["Output scores"], loc=9, bbox_to_anchor=(0, 1, 1, 0.1), labelcolor="#000") # TODO: Change square color
    fig.tight_layout()

    return fig


@app.route('/get_image/<string:job_id>')
def get_image(job_id=None):
    '''
    This function returns a PNG file from job results
    '''
    png=BytesIO()

    if job_id != None:
        result = result_from_job_id(job_id)
        numbers = []
        labels = []
        for data in result[::-1]:
            labels.append(data[0])
            numbers.append(data[1])

        bar_plt = bar_chart(numbers, labels)
        FigureCanvas(bar_plt).print_png(png)
        plt.close(plt.gcf())
    return Response(png.getvalue(),
    mimetype="image/png",
    headers={"Content-disposition":
                 "attachment; filename=plot.png"})
