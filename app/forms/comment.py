from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class Comment(FlaskForm):
    author_id = StringField(
        'author_id',
        validators=[DataRequired()]
    )
    content = StringField(
        'content',
        validators=[DataRequired()]
    )
    title = StringField(
        'title',
        validators=[DataRequired(), Length(max=128)]
    )
    is_reply = IntegerField(
        'title',
        validators=[DataRequired()]
    )
