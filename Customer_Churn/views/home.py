from flask import render_template,Blueprint,redirect,request,url_for,flash
from wtforms.validators import ValidationError
from Customer_Churn.forms.forms import AttributesForm
from flask_login import logout_user,login_required,current_user
from Customer_Churn.utilities.predict import gender_convert,string_to_int,predict_churn,clean_result
import pandas as pd
import numpy as np


home = Blueprint('home',__name__)

# @home.route('/',methods=["GET","POST"])
# @login_required
# def welcome():
#     return render_template('welcome.html')


# Home page where the user will input the parameters needed for predictions
@home.route('/',methods=['GET','POST'])
@login_required
def attributes():

    form = AttributesForm()

    if form.validate_on_submit():
# parameters for customer predictions
        credit_score = form.data.get('CreditScore')
        gender = gender_convert(form.data.get('Gender'))
        tenure = form.data.get('Tenure')
        age = form.data.get('Age')
        balance = form.data.get('Balance')
        num_products = form.data.get('NumOfProducts')
        credit_card = string_to_int(form.data.get('HasCrCard'))
        active = string_to_int(form.data.get('IsActiveMember'))
        salary = form.data.get('EstimatedSalary')

# create new customer instance for plug in
        customer = [[credit_score,gender,age,balance,tenure,num_products,credit_card,active,salary]]



        pred_churn = predict_churn()

        result = pred_churn.predict_customer(customer)


        return render_template('home.html',form=form, result=result,credit_score=credit_score,gender=gender,
        tenure=tenure,age=age,balance=balance,num_products=num_products,credit_card=credit_card,active=active,
        salary=salary)

    return render_template('home.html',form=form)

@home.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
