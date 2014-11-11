"""Department Class definition.
"""
from app import app
from db import db
from dept_emp import DeptEmp
from utils import current_records
from flask import g

class Departments(db.Model):
    dept_no = db.Column(db.String(4), primary_key=True)
    dept_name = db.Column(db.String(40))

    @property
    def employees(self):
        """Return a list of Employee numbers currently in this Department.
        """
        page = app.config['EMPLOYEES_PER_PAGE']
        emps = DeptEmp.query.filter_by(dept_no=self.dept_no)
        return [e.emp_no for e in current_records(emps, g.date)]
