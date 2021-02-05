from flask import Flask
from app.database.Database import Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configuration of CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Configuration of database
app.config.from_object(Database)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.entities.franchisor_entity import Franchisor, FranchisorModel
from app.entities.people_entity import People, PeopleModel
from app.controllers import peoples_controller, franchisor_controller

@app.shell_context_processor
def make_shell_context():
    return { 
        'db': db, 
        'FranchisorModel': FranchisorModel, 
        'PeopleModel': PeopleModel, 
        'Franchisor': Franchisor, 
        'People': People
        }