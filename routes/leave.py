from flask import Blueprint, request, jsonify
from models import db, leave

leave_bp = Blueprint('leave_bp', __name__)

@leave_bp.route('/', methods=['POST'])
def create_leave():
    data = request.get_json()
    new_leave = leave(**data)
    db.session.add(new_leave)
    db.session.commit()
    return jsonify(new_leave.serialize()), 201

@leave_bp.route('/', methods=['GET'])
def get_all_leave():
    leave_records = leave.query.all()
    return jsonify([leave.serialize() for leave in leave_records]), 200

@leave_bp.route('/<int:id>', methods=['GET'])
def get_leave(id):
    leave = leave.query.get(id)
    if not leave:
        return jsonify({'message': 'Leave record not found'}), 404
    return jsonify(leave.serialize()), 200

@leave_bp.route('/<int:id>', methods=['PUT'])
def update_leave(id):
    data = request.get_json()
    leave = leave.query.get(id)
    if not leave:
        return jsonify({'message': 'Leave record not found'}), 404
    for key, value in data.items():
        setattr(leave, key, value)
    db.session.commit()
    return jsonify(leave.serialize()), 200

@leave_bp.route('/<int:id>', methods=['DELETE'])
def delete_leave(id):
    leave = leave.query.get(id)
    if not leave:
        return jsonify({'message': 'Leave record not found'}), 404
    db.session.delete(leave)
    db.session.commit()
    return jsonify({'message': 'Leave record deleted'}), 200
