from flask import render_template,Blueprint,redirect,request,url_for
from Customer_Churn.forms.forms import AttributesForm
from flask_login import logout_user,login_required,current_user
from Customer_Churn.utilities.predict import gender_convert,clean_result,string_to_int,scaling
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np




home = Blueprint('home',__name__)

@home.route('/',methods=['GET','POST'])
@login_required
def attributes():


    form = AttributesForm()

    credit_score = form.data.get('CreditScore')
    gender = gender_convert(form.data.get('Gender'))
    # gender = form.data.get('Gender')
    tenure = form.data.get('Tenure')
    age = form.data.get('Age')
    balance = form.data.get('Balance')
    num_products = form.data.get('NumOfProducts')
    credit_card = string_to_int(form.data.get('HasCrCard'))
    active = string_to_int(form.data.get('IsActiveMember'))
    salary = form.data.get('EstimatedSalary')
    # exited = string_to_int(form.data.get('Exited'))
    customer = [[credit_score,gender,age,balance,tenure,num_products,credit_card,active,salary]]


    customer = scaling(customer)



    if form.validate_on_submit():
        model_predict = load_model('model')
        print(form.errors)
        pred = model_predict.predict(customer)


        print(pred[0][0])
        result = clean_result(pred[0][0])
        print(pred[0][0])

        return render_template('home.html',form=form, result=result,credit_score=credit_score,gender=gender,
        tenure=tenure,age=age,balance=balance,num_products=num_products,credit_card=credit_card,active=active,
        salary=salary)

    return render_template('home.html',form=form)

@home.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
