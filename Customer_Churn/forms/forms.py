from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from Customer_Churn.models import User


class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')

class AttributesForm(FlaskForm):
    # Surname = StringField('Surname',validators=[DataRequired()])
    CreditScore = IntegerField('Credit Score',validators=[DataRequired()])
    Gender = StringField('Gender',validators=[DataRequired()])
    Age = IntegerField('Age',validators=[DataRequired()])
    Tenure = IntegerField('Tenure',validators=[DataRequired()])
    Balance = IntegerField('Balance',validators=[DataRequired()])
    NumOfProducts = IntegerField('Number of Products',validators=[DataRequired()])
    HasCrCard = StringField('Has card?',validators=[DataRequired()])
    IsActiveMember = StringField('Is active?',validators=[DataRequired()])
    EstimatedSalary = IntegerField('Estimated Salary',validators=[DataRequired()])
    # Exited = StringField('Exited?',validators=[DataRequired()])
    submit = SubmitField('Run')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).field():
            raise ValidationError('Your username has been taken. Try another.')

class VisualParameters(FlaskForm):
    x_axis = SelectField(u'X',choices=[('CreditScore'),('Gender'),('Age'),('Tenure'),('Balance'),('NumOfProducts'),('HasCrCard'),
    ('IsActiveMember'),('EstimatedSalary'),('Exited')])
    y_axis = SelectField(u'Y',choices=[('CreditScore'),('Gender'),('Age'),('Tenure'),('Balance'),('NumOfProducts'),('HasCrCard'),
    ('IsActiveMember'),('EstimatedSalary'),('Exited')])
    z_axis = SelectField(u'Z',choices=[('CreditScore'),('Gender'),('Age'),('Tenure'),('Balance'),('NumOfProducts'),('HasCrCard'),
    ('IsActiveMember'),('EstimatedSalary'),('Exited')])
    submit = SubmitField('Run')

    
