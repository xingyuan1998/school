from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    content = StringField(
        'content',
        validators=[DataRequired()]
    )
    title = StringField(
        'title',
        validators=[DataRequired(), Length(max=128)]
    )

class ReplyForm(FlaskForm):
    content = StringField(
        'content',
        validators=[DataRequired()]
    )
    title = StringField(
        'title',
        validators=[DataRequired(), Length(max=128)]
    )
    comment_id = StringField(
        'comment_id',
        validators=[DataRequired(), Length(max=128)]
    )
