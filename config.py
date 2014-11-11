"""Configuration Information for the Kiosk. Edit as required.
Note: IN a production application, a mechamism would be provided to override
this external to the application, e.g. by setting Enviroment variables.
"""
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/employees'
DEBUG = True
SECRET_KEY = 'development key'
EMPLOYEES_PER_PAGE = 20