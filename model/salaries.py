"""Salary Class definition.
"""
from db import db

class Salaries(db.Model):
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'))
    salary = db.Column(db.Integer)
    from_date = db.Column(db.DateTime, primary_key=True)
    to_date = db.Column(db.DateTime)

    def __str__(self):
        return "{from_date} to {to_date}: {salary}".format(**self.__dict__)