from Customer_Churn import app
from Customer_Churn.utilities.predict import predict_churn

pc = predict_churn()
pc.train_create()


if __name__ == '__main__':
    app.run()
