from database import applications_collection  # Import from database.py
from datetime import datetime

class Application:
    def __init__(self, name, age, date, phone_number, issue, time, doctor_name):
        self.name = name
        self.age = age
        self.date = date
        self.phone_number = phone_number
        self.issue = issue
        self.time = time
        self.doctor_name = doctor_name

    def save_to_db(self):
        """
        Save the form data to the MongoDB collection 'applications'.
        """
        application_data = {
            "name": self.name,
            "age": self.age,
            "date": self.date,
            "phone_number": self.phone_number,
            "issue": self.issue,
            "time": self.time,
            "doctor_name": self.doctor_name,
            "created_at": datetime.now()  # Store the time when the form is submitted
        }

        # Use applications_collection from database.py to insert into the MongoDB collection
        applications_collection.insert_one(application_data)
