from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import SGD
from sklearn.metrics import classification_report,confusion_matrix
import pandas as pd
import numpy as np


df = pd.read_csv('Customer_Churn/churn.csv')
df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)

df.replace('Female',0,inplace=True)
df.replace('Male',1,inplace=True)

X = df[['CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']].values

y = df['Exited'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

scaler = MinMaxScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

epochs = 60
learning_rate = 0.2
decay_rate= learning_rate/epochs
momentum = 0.8

sgd = SGD(learning_rater=learning_rate,momentum=momentum,decay=decay_rate,nesterov=False)



def model():
    model = Sequential()

    # model.add(Dense(6,activation='relu'))
    model.add(Dense(6,activation='relu',input_dim = 9))
    model.add(Dense(6,activation='relu'))
    model.add(Dense(1,activation='sigmoid'))

    model.compile(optimizer=sgd,loss='binary_crossentropy',metrics=['accuracy'])

    return model

model = model()
model.fit(x=X_train,y=y_train,epochs=epochs)



model.save('model')

def scaling(var):

    var = scaler.transform(var)
    return var

def gender_convert(gender):
    zero = None
    one = None
    if gender == 'female' or 'Female':
        zero = 0
        return zero
    elif gender == "Male" or "male":
        one = 1
        return one
#
def string_to_int(var):
    zero = None
    one = None
    if var == 'yes' or 'Yes':
        one = 1
        return one
    elif var == 'no' or 'No':
        zero = 0
        return zero

def clean_result(v):

    x = round(v*100,2)

    return x
    # if x < 50.0:
    #     low = 'Low'
    #     return low
    # elif x > 50.0:
    #     high = 'High'
    #     return high
