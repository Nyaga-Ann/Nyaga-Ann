from models import db

class Employee(db.Model):
    __tablename__ = 'employees'
    Employee_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50), nullable=False)
    Last_Name = db.Column(db.String(50), nullable=False)
    Gender = db.Column(db.String(1))
    DOB = db.Column(db.Date)
    Marital_Status = db.Column(db.String(20))
    Address = db.Column(db.String(100))
    Contact = db.Column(db.String(15))
    Job_ID = db.Column(db.Integer, db.ForeignKey('job.Job_ID', ondelete='SET NULL'), nullable=False)
    Department_ID = db.Column(db.Integer, db.ForeignKey('department.Department_ID', ondelete='SET NULL'), nullable=False)
    Start_Date = db.Column(db.Date, nullable=False)
    End_Date = db.Column(db.Date)
    Employment_Status = db.Column(db.String(20))

def serialize(self):
        return {
            'Employee_ID': self.Employee_ID,
            'First_Name': self.First_Name,
            'Last_Name': self.Last_Name,
            'Gender': self.Gender,
            'DOB': self.DOB.isoformat() if self.DOB else None,
            'Marital_Status': self.Marital_Status,
            'Address': self.Address,
            'Contact': self.Contact,
            'Job_ID': self.Job_ID,
            'Department_ID': self.Department_ID,
            'Start_Date': self.Start_Date.isoformat() if self.Start_Date else None,
            'End_Date': self.End_Date.isoformat() if self.End_Date else None,
            'Employment_Status': self.Employment_Status
        }