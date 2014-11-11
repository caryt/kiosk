"""Employee Class definition.
"""
from db import db
from flask import g
from utils import years_between, current_record
from dept_manager import DeptManager
from dept_emp import DeptEmp


class Employees(db.Model):
    emp_no = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.DateTime)
    first_name = db.Column(db.String(14))
    last_name = db.Column(db.String(16))
    gender = db.Column(db.String(1))
    hire_date = db.Column(db.DateTime)
    salaries = db.relationship('Salaries')
    titles = db.relationship('Titles')

    @property
    def department(self):
        """Returns the current depertment for this employee, or None.
        """
        from departments import Departments
        depts = DeptEmp.query.filter_by(emp_no=self.emp_no).all()
        depts = current_record(depts, g.date)
        return None if depts is None else Departments.query.get(depts.dept_no)

    @property
    def manages(self):
        """Returns the current Department managed by this employee (if they
            are a manager), or None.
        """
        from departments import Departments
        depts = DeptManager.query.filter_by(emp_no=self.emp_no).all()
        depts = current_record(depts, g.date)
        return None if depts is None else Departments.query.get(depts.dept_no)

    def isValidCredentials(self, username, password):
        """Return True is username/password passed is valid for this employee.
        """
        return (username == self.username) and (password == self.password)

    @property
    def username(self):
        """Return the username (first_name.last_name) for this Employee.
        """
        return '%s.%s' % (self.first_name, self.last_name)

    @property
    def password(self):
        """Return the password (emp_no) for this employee.
        Note: This is not secure, only suitable for a sample application!
        """
        return str(self.emp_no)

    @property
    def dept_no(self):
        """Return the current Department Number for this Employee."""
        dept = self.department
        return None if dept is None else dept.dept_no

    @property
    def dept_name(self):
        """Return the current Department Name for this Employee."""
        dept = self.department
        return None if dept is None else dept.dept_name

    @property
    def job_title(self):
        """Return the current Job Title for this Employee."""
        title = current_record(self.titles, g.date)
        return None if title is None else title.title

    @property
    def years_with_company(self):
        """Return the Years with Company for this Employee."""
        return years_between(self.hire_date, g.date)

    @property
    def age(self):
        """Return the Age for this Employee."""
        return years_between(self.birth_date, g.date)

    @property
    def salary(self):
        """Return the current Salary for this Employee."""
        sal = current_record(self.salaries, g.date)
        return None if sal is None else sal.salary

    @property
    def isManager(self):
        """Return True if this Employee is currently a Manager."""
        return self.manages is not None

