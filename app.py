from flask import Flask
from config import Config

# Import the database and models
from models import db

# Import routes
from routes.attendance import attendance_bp
from routes.employee import employee_bp
from routes.employee_training import employee_training_bp
from routes.department import department_bp
from routes.job import job_bp
from routes.training import training_bp
from routes.payroll import payroll_bp
from routes.performance import performance_bp
from routes.leave import leave_bp
from routes.medical_records import medical_record_bp
from routes.report_management import report_management_bp

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the database with the app
    db.init_app(app)

    # Register blueprints for each set of routes
    app.register_blueprint(employee_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(training_bp)
    app.register_blueprint(employee_training_bp)
    app.register_blueprint(payroll_bp)
    app.register_blueprint(leave_bp)
    app.register_blueprint(report_management_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(medical_record_bp)
    app.register_blueprint(performance_bp)

    # Create the database tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


