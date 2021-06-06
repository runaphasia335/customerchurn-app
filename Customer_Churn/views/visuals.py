from flask import render_template,Blueprint,redirect,request,url_for
from Customer_Churn.forms.forms import AttributesForm,VisualParameters
from flask_login import current_user
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
# from plots import chart1,chart2,chart3,k_plot
from Customer_Churn.utilities.plots import chart1,chart2,chart3,k_plot
import json


visuals = Blueprint('visuals',__name__)

@visuals.route('/callback',methods=["GET","POST"])
def cb():
    return chart_cb(request.form.get('x_axis'),request.form.get('y_axis'))

@visuals.route('/visualizations',methods=['GET','POST'])
def charts():
    form = VisualParameters()
    df = pd.read_csv('Customer_Churn/churn.csv')
    df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)
    former = df.loc[df['Exited']==0]
    current = df.loc[df['Exited']==1]

    if form.x_axis.data is None and form.y_axis.data is None:
        x_axis = 'CreditScore'
        y_axis = 'CreditScore'
        z_axis = 'CreditScore'
    else:
        x_axis = form.data.get('x_axis')
        y_axis = form.data.get('y_axis')
        z_axis = form.data.get('z_axis')



    plot = chart1(x_axis,y_axis)
    plot2 = chart2(x_axis,y_axis,z_axis)
    plot3 = chart3(x_axis,y_axis)
    plot4 = k_plot(x_axis,y_axis)






    return render_template('graphs.html',plot=plot,plot2=plot2,plot3=plot3,plot4=plot4,form=form)
    # return render_template('graphs.html',plot=plot,form=form)
