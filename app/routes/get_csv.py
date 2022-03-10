import redis
import json
from flask import Response
from rq import Connection, Queue
from app import app
from config import Configuration



# Returns a CSV file from job results
@app.route('/get_CSV/<string:job_id>')
def get_CSV(job_id=None):
    
    csv="Error exporting CSV"
    if job_id != None:
        redis_url = Configuration.REDIS_URL
        redis_conn = redis.from_url(redis_url)
        with Connection(redis_conn):
            q = Queue(name=Configuration.QUEUE)
            result = q.fetch_job(job_id).result

        csv=""
        for data in result:
            csv+=str(data[0])+","+str(data[1])+"\n" # Formatting CSV properly

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=plot.csv"})