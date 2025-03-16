from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_reuploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
images=UploadSet('images',IMAGES)
    
class UploadForm(FlaskForm):
    file = FileField("image", validators=[
        FileRequired(), 
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    