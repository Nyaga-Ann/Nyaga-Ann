# models/attendance.py
from models import db
from datetime import date

class Attendance(db.Model):
    __tablename__ = 'attendance'
    Attendance_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Date = db.Column(db.Date, default=date.today)
    Status = db.Column(db.Enum('Present', 'Absent'), nullable=False)

    def serialize(self):
        return {
            'Attendance_ID': self.Attendance_ID,
            'Employee_ID': self.Employee_ID,
            'Date': self.Date,
            'Status': self.Status,
        }
