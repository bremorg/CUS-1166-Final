
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
# For AppointmentForm
from wtforms import DateTimeField
from wtforms.validators import ValidationError, DataRequired, Length




class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

# Appointments format is "date, time, duration, location, name, notes"
class AppointmentForm(FlaskForm):
    appointment_date = DateTimeField('appointment_date', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    appointment_dur = DateTimeField('appointment_dur', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    appointment_loc = StringField('appointment_loc', validators=[DataRequired()])
    appointment_client = StringField('appointment_client', validators=[DataRequired()])
    appointment_desc = StringField('appointment_desc')
    submit = SubmitField('submit')
