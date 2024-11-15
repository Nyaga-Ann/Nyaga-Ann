from models import db

class ReportManagement(db.Model):
    __tablename__ = 'report_management'
    Report_ID = db.Column(db.Integer, primary_key=True)
    Report_Type = db.Column(db.Enum('Performance', 'Training', 'Leave', 'Conduct'), nullable=False)
    Employee_ID = db.Column(db.Integer, db.ForeignKey('employees.Employee_ID', ondelete='SET NULL'))
    Created_By = db.Column(db.Integer, db.ForeignKey('users.User_ID', ondelete='SET NULL'), nullable=False)
    Report_Date = db.Column(db.Date, nullable=False)
    Report_Content = db.Column(db.Text, nullable=False)
    Status = db.Column(db.Enum('Draft', 'Finalized'), default='Draft')

def serialize(self):
        return {
            'Report_ID': self.Report_ID,
            'Report_Type': self.Report_Type,
            'Employee_ID': self.Employee_ID,
            'Created_By': self.Created_By,
            'Report_Date': self.Report_Date,
            'Report_Content': self.Report_Content,
            'Status': self.Status,
        }
