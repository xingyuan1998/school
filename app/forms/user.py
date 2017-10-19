from flask_wtf import FlaskForm
from wtforms import StringField


class RegForm(FlaskForm):
    password = StringField(
        'password'
    )
    student_id = StringField(
        'student_id'
    )

