from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_redis import FlaskRedis
import  os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY']='hard to guess string'
app.config['UP_DIR']=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config['FC_DIR']=os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/face/")
app.config["REDIS_URL"] = "redis://192.168.1.101:6379/0"
app.debug = True

db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.home import home as home_blueprint
from app.admin import admin  as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
