
#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))

# Record appointments (date, time, duration, location, name, notes) to database
class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.DateTime, index=True)
    appointment_dur = db.Column(db.DateTime)
    appointment_loc = db.Column(db.String(128), index=True)
    appointment_client = db.Column(db.String(128), index=True)
    appointment_desc = db.Column(db.String(128), index=True)
