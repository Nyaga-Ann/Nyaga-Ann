from models import db

class EmployeeTraining(db.Model):
    __tablename__ = 'employee_training'
    Record_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Training_ID = db.Column(db.Integer, db.ForeignKey('training.Training_ID', ondelete='SET NULL'), nullable=False)
    Completion_Status = db.Column(db.Enum('Completed', 'Pending'), nullable=False)
    Certification = db.Column(db.String(50))

def serialize(self):
        return {
            'Record_ID': self.Record_ID,
            'Employee_ID': self.Employee_ID,
            'Training_ID': self.Training_ID,
            'Completion_Status': self.Completion_Status,
            'Certification': self.Certification,
        }