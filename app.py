from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from datetime import timedelta

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

MONGODB_SETTINGS = {
    'db':'AwesomeCompanyDb',
    'host':'localhost',
    'port':27017    
}

app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS

initialize_db(app)
initialize_routes(api)

app.run()