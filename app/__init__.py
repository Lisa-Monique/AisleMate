from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
import os
from flask.ext.login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)
lm = LoginManager()
lm.init_app(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
lm.login_view = 'index'

@lm.user_loader
def load_user(user_id):
  user = models.User.query.filter(models.User.id == int(user_id)).first()
  return user
