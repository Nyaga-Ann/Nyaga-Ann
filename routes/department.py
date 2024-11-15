from flask import Blueprint, request, jsonify
from models import db, Department

department_bp = Blueprint('department_bp', __name__)

@department_bp.route('/', methods=['POST'])
def create_department():
    data = request.get_json()
    new_department = Department(**data)
    db.session.add(new_department)
    db.session.commit()
    return jsonify(new_department.serialize()), 201

@department_bp.route('/', methods=['GET'])
def get_all_departments():
    departments = Department.query.all()
    return jsonify([department.serialize() for department in departments]), 200

@department_bp.route('/<int:id>', methods=['GET'])
def get_department(id):
    department = Department.query.get(id)
    if not department:
        return jsonify({'message': 'Department not found'}), 404
    return jsonify(department.serialize()), 200

@department_bp.route('/<int:id>', methods=['PUT'])
def update_department(id):
    data = request.get_json()
    department = Department.query.get(id)
    if not department:
        return jsonify({'message': 'Department not found'}), 404
    for key, value in data.items():
        setattr(department, key, value)
    db.session.commit()
    return jsonify(department.serialize()), 200

@department_bp.route('/<int:id>', methods=['DELETE'])
def delete_department(id):
    department = Department.query.get(id)
    if not department:
        return jsonify({'message': 'Department not found'}), 404
    db.session.delete(department)
    db.session.commit()
    return jsonify({'message': 'Department deleted'}), 200
