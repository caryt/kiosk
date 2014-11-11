from db import db

class Titles(db.Model):
    emp_no = db.Column(db.Integer, db.ForeignKey('employees.emp_no'))
    title = db.Column(db.String(50))
    from_date = db.Column(db.DateTime, primary_key=True)
    to_date = db.Column(db.DateTime)

    def __str__(self):
        return "{from_date} to {to_date}: {title}".format(**self.__dict__)