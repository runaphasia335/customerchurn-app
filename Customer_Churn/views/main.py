from flask import render_template,Blueprint,redirect,request,url_for
from flask_login import login_user, current_user, logout_user, login_required
from Customer_Churn.forms.forms import LoginForm,RegistrationForm
from Customer_Churn.models import User
from Customer_Churn import db
# from Customer_Churn.utilities.predict import model

main = Blueprint('main', __name__)
# login page if user is not logged in
@main.route('/login',methods=['GET',"POST"])
def login():
   form = LoginForm()
   print('validating')
   if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user.check_password(form.password.data) and user is not None:
         login_user(user)
         next = request.args.get('next')

         if next == None or not next[0] == '/':
            next =  url_for('home.attributes')
         return redirect(next)
   return render_template('index.html',form=form)


# registration page. after registration, user will be redirected to login page
@main.route('/register',methods=['GET','POST'])
def register():
   form = RegistrationForm()
   print('validating')
   if form.validate_on_submit():
      user = User(username=form.username.data, password=form.password.data)
      db.session.add(user)
      db.session.commit()
      print('user added')

      return redirect(url_for('main.login'))
   print('routing to register.html')
   return render_template('register.html',form=form)
