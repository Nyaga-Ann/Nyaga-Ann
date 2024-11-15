from models import db

class MedicalRecords(db.Model):
    __tablename__ = 'medical_records'
    Record_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Medical_Condition = db.Column(db.String(100))
    Emergency_Contact = db.Column(db.String(100))
    Emergency_Contact_Relationship = db.Column(db.String(50))
    Emergency_Contact_Phone = db.Column(db.String(15))
    Last_Medical_Check = db.Column(db.Date)

def serialize(self):
        return {
            'Record_ID': self.Record_ID,
            'Employee_ID': self.Employee_ID,
            'Medical_Condition': self.Medical_Condition,
            'Emergency_Contact': self.Emergency_Contact,
            'Emergency_Contact_Relationship': self.Emergency_Contact_Relationship,
            'Emergency_Contact_Phone': self.Emergency_Contact_Phone,
            'Last_Medical_Check': self.Last_Medical_Check,
        }