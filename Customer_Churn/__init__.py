from flask import Flask
import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# app = dash.Dash(__name__)
app = Flask(__name__)
# app = dash.Dash(__name__,server=server)
app.config['SECRET_KEY'] ='mysecret'

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

# login config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'




from Customer_Churn.views.main import main
from Customer_Churn.views.home import home
from Customer_Churn.views.visuals import visuals

app.register_blueprint(main)
app.register_blueprint(home)
app.register_blueprint(visuals)
