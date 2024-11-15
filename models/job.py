from models import db

class Job(db.Model):
    __tablename__ = 'job'
    Job_ID = db.Column(db.Integer, primary_key=True)
    Job_Title = db.Column(db.String(50), nullable=False)
    Department_ID = db.Column(db.Integer, db.ForeignKey('department.Department_ID', ondelete='SET NULL'))
    Description = db.Column(db.Text)

def serialize(self):
        return {
            'Job_ID': self.Job_ID,
            'Job_Title': self.Job_Title,
            'Department_ID': self.Department_ID,
            'Description': self.Description,
        }
