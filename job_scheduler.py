import time
import schedule
import os
from dotenv import load_dotenv

load_dotenv()

job_in_progress = False

batch_size = int(os.environ.get('BATCH_SIZE'))
run_frequency_in_seconds = int(os.environ.get('RUN_FREQUENCY_IN_SECONDS'))

class JobScheduler:
    def __init__(self, job_processor):
        self.submitted_jobs = []
        self.completed_jobs = []
        self.job_processor = job_processor

    def submit(self, job):
        self.submitted_jobs.append(job)

    def run(self):
        print("Scheduler started ... ")
        schedule.every(run_frequency_in_seconds).seconds.do(self.batch)  # Adjust interval as needed
        while True:
            schedule.run_pending()
            time.sleep(1)  # Avoid busy waiting

    def batch(self):
        global job_in_progress
        if not job_in_progress:
            job_in_progress = True
            print("Job started...")
            print("There are "+ str(len(self.submitted_jobs)) + " jobs in the queue. ")
            if self.submitted_jobs is not None and len(self.submitted_jobs) != 0:
                max_3_items = self.submitted_jobs[
                              :min(3, len(self.submitted_jobs))]  # Slice up to the minimum length or the list length
                if max_3_items is not None and len(max_3_items) != 0:
                    for item in max_3_items:
                        print(item)

                        self.job_processor.process(item)

                        self.completed_jobs.append(item)
                        self.submitted_jobs.remove(item)
                    print("Job completed...")
            job_in_progress = False
