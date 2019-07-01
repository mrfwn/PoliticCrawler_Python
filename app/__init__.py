from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_cors import CORS


UPLOAD_FOLDER = '/'
app = Flask(__name__)

app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controllers import default