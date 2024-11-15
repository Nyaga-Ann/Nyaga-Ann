from flask import Blueprint

# Import blueprints for each model
from .attendance import attendance_bp
from .employee import employee_bp
from .employee_training import employee_training_bp
from .department import department_bp
from .job import job_bp
from .training import training_bp
from .payroll import payroll_bp
from .performance import performance_bp
from .leave import leave_bp
from .medical_records import medical_record_bp
from .report_management import report_management_bp
from .training import training_bp

# Create a main blueprint for all routes
main_bp = Blueprint('main', __name__)

# Register each blueprint with the main app
def register_blueprints(app):
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(department_bp, url_prefix='/departments')
    app.register_blueprint(job_bp, url_prefix='/jobs')
    app.register_blueprint(training_bp, url_prefix='/trainings')
    app.register_blueprint(payroll_bp, url_prefix='/payrolls')
    app.register_blueprint(leave_bp, url_prefix='/leaves')
    app.register_blueprint(report_management_bp, url_prefix='/reports')
