from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize key objects
app = Flask(__name__)
db = SQLAlchemy(app)

# Configure Flask app
app.config.from_object(Config)
db = SQLAlchemy(app)

# Imports to prevent circular dependency
from app import views
from app import models

# Create the database tables
db.create_all()