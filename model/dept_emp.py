"""Class Definition for Table managing many-to-many
relationship between Departments and the Employees in them.
"""
from db import db

class DeptEmp(db.Model):
    dept_no = db.Column(db.String(4), db.ForeignKey('departments.dept_no'), primary_key=True)
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'), primary_key=True)
    from_date = db.Column(db.DateTime)
    to_date = db.Column(db.DateTime)