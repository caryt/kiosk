"""Using the MySQL Employees sample database this application
allows you to login to the site and view your details.
If you are a manager of a department then you have the ability
to view your details as well as all employees of that department.
"""
from app import app
from model import Employees, Departments
from flask import request, session, g, redirect, url_for, render_template, flash

from datetime import date

@app.before_request
def before_request():
    """Set `g.date` to the current date for every request.
    This allows future flexibility to specify an effectie date other than today
    """
    g.date = date.today()
    session['logging_in'] = False

@app.route('/', methods=['GET', 'POST'])
def login():
    """GET: Display Login page.
    POST: Log n by validating username/password. Saves the emp_no logged in as.
    """
    error = None
    session['logging_in'] = True
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        emp = Employees.query.get(password)
        if emp is not None and emp.isValidCredentials(username, password):
            session['logged_in'] = True
            session['emp_no'] = emp.emp_no
            flash('You were logged in')
            return redirect(url_for('department', page=1))
        else:
            error = 'Invalid username / password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """Logout of the web site."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/department/<int:page>')
def department(page=1):
    """Display employee details for the current employee, or list of employees
    in their department if they are a manager.
    """
    emp = Employees.query.get(session.get('emp_no', ''))
    if emp is not None and emp.isManager:
        dept = Departments.query.get(emp.dept_no)
        size = app.config['EMPLOYEES_PER_PAGE']
        employees = dept.employees
        total = len(employees)
        employees = dept.employees[ (page - 1) * size : page * size ]
        employees = [Employees.query.get(emp_no) for emp_no in employees]
        return render_template('department.html',
            dept_name = dept.dept_name,
            employees = employees,
            page = page,
            size = size,
            total = total,
            )
    else:
        return render_template('employee.html', emp=emp)

@app.route('/emp/<emp_no>')
def emp(emp_no):
    """View a single employee."""
    emp = Employees.query.get(emp_no)
    return render_template('employee.html', emp=emp)

if __name__ == '__main__':
    app.run()