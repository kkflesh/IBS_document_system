from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField


class UpdateISO(FlaskForm):
    file = FileField()
    submit = SubmitField('Upload')
