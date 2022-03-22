from flask import Response
from app import app
from app.utils.result_from_job_id import result_from_job_id
import json

# Returns a JSON file from job results
@app.route('/get_json/<string:job_id>')
def get_json(job_id=None):
    
    res=json.dumps({"status": "false", "description": "Error exporting JSON"})
    if job_id != None:
        
        result = result_from_job_id(job_id)
        res = json.dumps(dict(result))

    return Response(
        res,
        mimetype="text/json",
        headers={"Content-disposition":
                 "attachment; filename=plot.json"})