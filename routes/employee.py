from flask import Blueprint, request, jsonify
from models import db, Employee

employee_bp = Blueprint('employee_bp', __name__)

@employee_bp.route('/', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.serialize()), 201

@employee_bp.route('/', methods=['GET'])
def get_all_employees():
    employees = Employee.query.all()
    return jsonify([employee.serialize() for employee in employees]), 200

@employee_bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    return jsonify(employee.serialize()), 200

@employee_bp.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify(employee.serialize()), 200

@employee_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'}), 404
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'}), 200
