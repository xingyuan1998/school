from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Length


class RegForm(FlaskForm):
    password = StringField(
        'password',
        validators=[DataRequired(), Length(max=128)]
    )
    student_id = StringField(
        'student_id',
        validators=[DataRequired(), Length(max=64)]
    )


class ChangePwdForm(FlaskForm):
    last_pwd = StringField(
        'last_pwd',
        validators=[DataRequired(), Length(max=128)]
    )
    now_pwd = StringField(
        'now_pwd',
        validators=[DataRequired(), Length(max=64)]
    )
