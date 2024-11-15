from models import db

class Department(db.Model):
    __tablename__ = 'department'
    Department_ID = db.Column(db.Integer, primary_key=True)
    Department_Name = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.Text)

def serialize(self):
        return {
            'Department_ID': self.Department_ID,
            'Department_Name': self.Department_Name,
            'Description': self.Description,
        }