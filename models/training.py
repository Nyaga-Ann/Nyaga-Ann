from models import db

class Training(db.Model):
    __tablename__ = 'training'
    Training_ID = db.Column(db.Integer, primary_key=True)
    Training_Type = db.Column(db.Enum('Online', 'In Office', 'Outside'), nullable=False)
    Location = db.Column(db.String(100))
    Date = db.Column(db.Date)
    Time = db.Column(db.Time)
    Requirements = db.Column(db.Text)
    Points = db.Column(db.Integer)

def serialize(self):
        return {
            'Training_ID': self.Training_ID,
            'Training_Type': self.Training_Type,
            'Location': self.Location,
            'Date': self.Date,
            'Time': self.Time,
            'Requirements': self.Requirements,
            'Points': self.Points,
        }
