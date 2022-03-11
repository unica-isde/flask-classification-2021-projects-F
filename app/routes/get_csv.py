from flask import Response
from app import app
from app.utils.result_from_job_id import result_from_job_id


# Returns a CSV file from job results
@app.route('/get_CSV/<string:job_id>')
def get_CSV(job_id=None):
    
    csv="Error exporting CSV"
    if job_id != None:
        
        result = result_from_job_id(job_id)
        csv=""
        for data in result:
            csv+=str(data[0])+","+str(data[1])+"\n" # Formatting CSV properly

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=plot.csv"})