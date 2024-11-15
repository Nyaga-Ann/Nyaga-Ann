from flask import Blueprint, request, jsonify
from models import db, EmployeeTraining

employee_training_bp = Blueprint('employee_training_bp', __name__)

@employee_training_bp.route('/', methods=['POST'])
def create_employee_training():
    data = request.get_json()
    new_employee_training = EmployeeTraining(**data)
    db.session.add(new_employee_training)
    db.session.commit()
    return jsonify(new_employee_training.serialize()), 201

@employee_training_bp.route('/', methods=['GET'])
def get_all_employee_training():
    employee_trainings = EmployeeTraining.query.all()
    return jsonify([training.serialize() for training in employee_trainings]), 200

@employee_training_bp.route('/<int:id>', methods=['GET'])
def get_employee_training(id):
    employee_training = EmployeeTraining.query.get(id)
    if not employee_training:
        return jsonify({'message': 'Employee training record not found'}), 404
    return jsonify(employee_training.serialize()), 200

@employee_training_bp.route('/<int:id>', methods=['PUT'])
def update_employee_training(id):
    data = request.get_json()
    employee_training = EmployeeTraining.query.get(id)
    if not employee_training:
        return jsonify({'message': 'Employee training record not found'}), 404
    for key, value in data.items():
        setattr(employee_training, key, value)
    db.session.commit()
    return jsonify(employee_training.serialize()), 200

@employee_training_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee_training(id):
    employee_training = EmployeeTraining.query.get(id)
    if not employee_training:
        return jsonify({'message': 'Employee training record not found'}), 404
    db.session.delete(employee_training)
    db.session.commit()
    return jsonify({'message': 'Employee training record deleted'}), 200
