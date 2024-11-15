from flask import Blueprint, request, jsonify
from models import db, Payroll

payroll_bp = Blueprint('payroll_bp', __name__)

@payroll_bp.route('/', methods=['POST'])
def create_payroll():
    data = request.get_json()
    new_payroll = Payroll(**data)
    db.session.add(new_payroll)
    db.session.commit()
    return jsonify(new_payroll.serialize()), 201

@payroll_bp.route('/', methods=['GET'])
def get_all_payroll():
    payroll_records = Payroll.query.all()
    return jsonify([record.serialize() for record in payroll_records]), 200

@payroll_bp.route('/<int:id>', methods=['GET'])
def get_payroll(id):
    payroll = Payroll.query.get(id)
    if not payroll:
        return jsonify({'message': 'Payroll record not found'}), 404
    return jsonify(payroll.serialize()), 200

@payroll_bp.route('/<int:id>', methods=['PUT'])
def update_payroll(id):
    data = request.get_json()
    payroll = Payroll.query.get(id)
    if not payroll:
        return jsonify({'message': 'Payroll record not found'}), 404
    for key, value in data.items():
        setattr(payroll, key, value)
    db.session.commit()
    return jsonify(payroll.serialize()), 200

@payroll_bp.route('/<int:id>', methods=['DELETE'])
def delete_payroll(id):
    payroll = Payroll.query.get(id)
    if not payroll:
        return jsonify({'message': 'Payroll record not found'}), 404
    db.session.delete(payroll)
    db.session.commit()
    return jsonify({'message': 'Payroll record deleted'}), 200
