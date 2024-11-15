from models import db

class Payroll(db.Model):
    __tablename__ = 'payroll'
    Payroll_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Basic_Salary = db.Column(db.Numeric(10, 2), nullable=False)
    Deductions = db.Column(db.Numeric(10, 2))
    Net_Pay = db.Column(db.Numeric(10, 2))
    Pay_Date = db.Column(db.Date)

def serialize(self):
        return {
            'Payroll_ID': self.Payroll_ID,
            'Employee_ID': self.Employee_ID,
            'Basic_Salary': self.Basic_Salary,
            'Deductions': self.Deductions,
            'Net_Pay': self.Net_Pay,
            'Pay_Date': self.Pay_Date,
        }