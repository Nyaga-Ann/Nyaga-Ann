from models import db

class EmpLeave(db.Model):
    __tablename__ = 'emp_leave'
    Leave_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Leave_Type = db.Column(db.Enum('Sick', 'Casual', 'Annual', 'Maternity'), nullable=False)
    Start_Date = db.Column(db.Date, nullable=False)
    End_Date = db.Column(db.Date)
    Status = db.Column(db.Enum('Approved', 'Pending', 'Declined'), default='Pending')
    Remarks = db.Column(db.Text)

def serialize(self):
        return {
            'Leave_ID': self.Leave_ID,
            'Employee_ID': self.Employee_ID,
            'Leave_Type': self.Leave_Type,
            'Start_Date': self.Start_Date,
            'End_Date': self.End_Date,
            'Status': self.Status,
            'Remarks': self.Remarks,
        }
