from models import db


class Performance(db.Model):
    __tablename__ = 'performance'
    Performance_ID = db.Column(db.Integer, primary_key=True)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'), nullable=False)
    Objective = db.Column(db.Text, nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    Comments = db.Column(db.Text)
    Review_Date = db.Column(db.Date)

def serialize(self):
        return {
            'Performance_ID': self.Performance_ID,
            'Employee_ID': self.Employee_ID,
            'Objective': self.Objective,
            'Rating': self.Rating,
            'Comments': self.Comments,
            'Review_Date': self.Review_Date,
        }
