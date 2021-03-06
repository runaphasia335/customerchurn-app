
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import joblib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ReduceLROnPlateau
from sklearn.metrics import classification_report,confusion_matrix
import pandas as pd
import numpy as np

class predict_churn():

    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.result = None


    def __str__(self):
        return str(self.result[0][0])
# NN model will be created here. Dataset will be cleaned, model will be trained.
    def train_create(self):

        df = pd.read_csv('Customer_Churn/churn.csv')
        df.drop(['RowNumber','Surname','Geography','CustomerId'],axis=1,inplace=True)

        df.replace('Female',0,inplace=True)
        df.replace('Male',1,inplace=True)

        X = df[['CreditScore','Gender','Age','Tenure','Balance','NumOfProducts','HasCrCard','IsActiveMember','EstimatedSalary']].values

        y = df['Exited'].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=10)

# MinMaxScaler instance created, fitted then saved for later use

        scale = MinMaxScaler()

        scale.fit(self.X_train)

        joblib.dump(scale,"model_scale.xz")
# <----------------------------------------------------------->

        self.X_train = scale.transform(self.X_train)

        self.X_test = scale.transform(self.X_test)

# model creation ------------------------------>
        epochs = 200
        learning_rate = 0.2
        decay_rate= learning_rate/epochs
        momentum = 0.8

        rlrop = ReduceLROnPlateau(monitor='val_loss',factor=0.1,patience=100)

        sgd = SGD(learning_rate=learning_rate,momentum=momentum,decay=decay_rate,nesterov=False)



        model = Sequential()

    # model.add(Dense(6,activation='relu'))
        model.add(Dense(6,activation='relu',input_dim = 9))
        model.add(Dense(6,activation='relu'))
        model.add(Dense(1,activation='sigmoid'))

        model.compile(optimizer=sgd,loss='binary_crossentropy',metrics=['accuracy'])

        model.fit(x=self.X_train,y=self.y_train,batch_size=64,steps_per_epoch=10,epochs=epochs,callbacks=[rlrop])

    # model saved after trained and fitted
        model.save('model.h5')


# function will be called after form validation is completed
    def predict_customer(self,v1):
        scaler = joblib.load("model_scale.xz")

        customer = scaler.transform(v1)

        pred = load_model('model.h5')

        self.result = pred.predict(customer)

        result = int(self.result)

        return clean_result(result)



# converts Gender column values into integers
def gender_convert(gender):
    zero = None
    one = None
    if gender == 'female' or 'Female':
        zero = 0
        return zero
    elif gender == "Male" or "male":
        one = 1
        return one


# converts strings to integers
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

    if x < 50.0:
        low = 'Low'
        return low
    elif x > 50.0:
        high = 'High'
        return high
