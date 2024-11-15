from flask import Blueprint, request,jsonify
from models import db, Attendance

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route('/', methods=['POST'])
def create_attendance():
    data = request.get_json()
    new_attendance = Attendance(**data)
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify(new_attendance.serialize()),201

@attendance_bp.route('/', methods=['GET'])
def get_all_attendance():
    attendance_records = Attendance.query.all()
    return jsonify([record.serialize() for record in attendance_records]), 200

@attendance_bp.route('/<int:id>', methods=['GET'])
def get_attendance(id):
    attendance = Attendance.query.get(id)
    if not attendance:
        return jsonify({'message': 'Attendance record not found'}), 404
    return jsonify(attendance.serialize()), 200

@attendance_bp.route('/<int:id>', methods=['PUT'])
def update_attendance(id):
    data = request.get_json()
    attendance = Attendance.query.get(id)
    if not attendance:
        return jsonify({'message': 'Attendance record not found'}), 404
    for key, value in data.items():
        setattr(attendance, key, value)
    db.session.commit()
    return jsonify(attendance.serialize()), 200

@attendance_bp.route('/<int:id>', methods=['DELETE'])
def delete_attendance(id):
    attendance = Attendance.query.get(id)
    if not attendance:
        return jsonify({'message': 'Attendance record not found'}), 404
    db.session.delete(attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance record deleted'}), 200