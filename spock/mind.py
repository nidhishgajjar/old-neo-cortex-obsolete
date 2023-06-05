from spock.mindflow import MindFlow
from spock.job_manager import JobManager
from thinkfast.initialize import ThinkFast
from thinkslow.initialize import ThinkSlow

def mind(user_input, context):
    livelymind = ThinkFast(user_input, context)
    lazymind = ThinkSlow(user_input)
    job_manager = JobManager()
    return MindFlow(user_input, context, livelymind, lazymind, job_manager)