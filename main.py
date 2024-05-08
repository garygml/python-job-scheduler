from fastapi import FastAPI
from job_scheduler import JobScheduler
from summarization_job_processor import SummarizationJobDefinition, SummarizationJobProcessor
from datetime import datetime

app = FastAPI()

summarization_job_processor = SummarizationJobProcessor()
scheduler = JobScheduler(summarization_job_processor)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/list-submitted-jobs")
def list_submitted_jobs():
    return scheduler.submitted_jobs


@app.get("/list-completed-jobs")
def list_completed_jobs():
    return scheduler.completed_jobs


@app.get("/test-submit")
def submit():
    new_job_1 = SummarizationJobDefinition("/input",
                                           "/output",
                                           datetime.now(),
                                           "new_job_1")
    new_job_2 = SummarizationJobDefinition("/input2",
                                           "/output2",
                                           datetime.now(),
                                           "new_job_2")
    new_job_3 = SummarizationJobDefinition("/input3",
                                           "/output3",
                                           datetime.now(),
                                           "new_job_3")
    scheduler.submit(new_job_1)
    scheduler.submit(new_job_2)
    scheduler.submit(new_job_3)

    return scheduler.submitted_jobs


@app.get("/run")
def run():
    scheduler.run()
