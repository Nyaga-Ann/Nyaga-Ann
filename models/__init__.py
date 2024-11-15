from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Import models
from .department import Department
from .job import Job
from .employee import Employee
from .payroll import Payroll
from .performance import Performance
from .report_management import ReportManagement
from .employee_training import EmployeeTraining
from .training import Training
from .attendance import Attendance
from .leave import EmpLeave
from .medical_records import MedicalRecords
