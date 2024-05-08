import datetime
import time

class SummarizationJobDefinition:
    def __init__(self, input_location: str, output_location: str, timestamp: datetime, description: str):
        self.input_location = input_location
        self.output_location = output_location
        self.timestamp = timestamp
        self.description = description

    def __str__(self):
        return f"{self.timestamp} - {self.input_location} -> {self.output_location}"

class SummarizationJobProcessor:
    def process(self, item):
        print("input location: " + item.input_location)
        print("output location: "+ item.output_location)
        # Need to implement the actual code to run jobs
        time.sleep(2)
        print("Job Completed. ")
