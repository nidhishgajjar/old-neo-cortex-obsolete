class JobManager:
    def __init__(self):
        self.jobs = {}

    def add_job(self, user_input):
        if len(self.jobs) < 2:
            job_id = len(self.jobs)
            self.jobs[job_id] = user_input
            return job_id
        else:
            return None

    def remove_job(self, job_id):
        if job_id in self.jobs:
            del self.jobs[job_id]
            return True
        else:
            return False

    def get_job_count(self):
        return len(self.jobs)