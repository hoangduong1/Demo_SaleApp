from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary


app = Flask(__name__)
app.secret_key = '4567890sdfghjklcvbnvb4567fg6yug'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/it02saledbv1?charset=utf8mb4' % quote('duong1')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

cloudinary.config(cloud_name='dmfr3gngl', api_key='119749293867732', api_secret='R42-4n6WSoV-ChzSKYws7Nqy0g4')

babel = Babel(app=app)


@babel.localeselector
def load_locale():
    return "vi"
