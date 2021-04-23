"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import SelectField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from .models import db, User


def user_choices():
    output_list = []
    result = db.session.query(User).all()
    for row in result:
        output_list.append((row.id, row.name))
    return output_list


class DashboardForm(FlaskForm):
    """Test to populate from from db data"""
    # name = StringField('Users', validators=[DataRequired(), ])
    name = SelectField('boat_type', choices=user_choices(), validators=[DataRequired(), ])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select a stronger password.')
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    website = StringField(
        'Website',
        validators=[Optional()]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
