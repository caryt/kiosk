from db import db
from flask import g

Dept_Manager = db.Table('Dept_Manager',
    db.Column('dept_no', db.String(4), db.ForeignKey('departments.dept_no')),
    db.Column('emp_no', db.Integer, db.ForeignKey('employees.emp_no')),
    db.Column('from_date', db.DateTime),
    db.Column('to_date', db.DateTime),
)

Dept_Emp = db.Table('Dept_Emp',
    db.Column('dept_no', db.String(4), db.ForeignKey('departments.dept_no')),
    db.Column('emp_no', db.Integer, db.ForeignKey('employees.emp_no')),
    db.Column('from_date', db.DateTime),
    db.Column('to_date', db.DateTime),
)

class Employees(db.Model):
    emp_no = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.DateTime)
    first_name = db.Column(db.String(14))
    last_name = db.Column(db.String(16))
    gender = db.Column(db.String(1))
    hire_date = db.Column(db.DateTime)
    salaries = db.relationship('Salaries', backref='employees', lazy='select')
    titles = db.relationship('Titles', backref='titles', lazy='select')
    managers = db.relationship('Departments', secondary=Dept_Manager, backref=db.backref('mgrs', lazy='select'), lazy='select')
    departments = db.relationship('Departments', secondary=Dept_Emp, backref=db.backref('depts', lazy='select'), lazy='select')

    def isValidCredentials(self, username, password):
        return (username == self.username) and (password == self.password)

    @property
    def username(self):
        return '%s.%s' % (self.first_name, self.last_name)

    @property
    def password(self):
        return str(self.emp_no)

    @property
    def dept_no(self):
        for dept in self.departments:
            return dept.dept_no
            if dept.from_date < g.date:
                return dept
        return None

    @property
    def dept_name(self):
        for dept in self.departments:
            return dept.dept_name
            if dept.from_date < g.date:
                return dept
        return None

    @property
    def job_title(self):
        for title in self.titles:
            if title.from_date < g.date:
                return title
        return None

    @property
    def years_with_company(self):
        return self.years_between(self.hire_date, g.date)

    @property
    def age(self):
        return self.years_between(self.birth_date, g.date)

    @property
    def salary(self):
        for sal in self.salaries:
            if sal.from_date < g.date:
                return sal
        return None

    @property
    def isManager(self):
        return self.managers != None

    def years_between(self, frm, to):
        return to.year - frm.year - ((to.month, to.day) < (frm.month, frm.day))
