from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, equal_to
from flask_wtf.file import FileField


class LoginForm(FlaskForm):
    username = StringField("Enter Username")
    password = PasswordField("Enter Password")
    login = SubmitField("Authorization")


class RegisterForm(FlaskForm):
    profile_image = FileField("Upload File")
    username = StringField("Enter username", validators=[DataRequired()])
    password = PasswordField("Enter password", validators=[DataRequired(), Length(min=8, max=64)])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(),
                                                                   equal_to("password",
                                                                            message="Repeat password and password do not match")])

    register = SubmitField("Registration")
