"""Initialise the Database object.
"""
from app import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
