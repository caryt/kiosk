"""Create the Application object and set its configuration.
"""
from flask import Flask

app = Flask('__main__')
app.config.from_object('config')
