import redis
from rq import Connection, Queue
from config import Configuration


# Return result of a task given the job_id
def result_from_job_id(job_id):

    redis_url = Configuration.REDIS_URL
    redis_conn = redis.from_url(redis_url)
    with Connection(redis_conn):
        q = Queue(name=Configuration.QUEUE)
        try:
            result = q.fetch_job(job_id).result
            return result
        except:
            return list()
