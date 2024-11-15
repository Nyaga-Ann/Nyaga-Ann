from flask import Blueprint, request, jsonify
from models import db, MedicalRecords

medical_record_bp = Blueprint('medical_record_bp', __name__)

@medical_record_bp.route('/', methods=['POST'])
def create_medical_record():
    data = request.get_json()
    new_medical_record = MedicalRecords(**data)
    db.session.add(new_medical_record)
    db.session.commit()
    return jsonify(new_medical_record.serialize()), 201

@medical_record_bp.route('/', methods=['GET'])
def get_all_medical_records():
    medical_records = MedicalRecords.query.all()
    return jsonify([record.serialize() for record in medical_records]), 200

@medical_record_bp.route('/<int:id>', methods=['GET'])
def get_medical_record(id):
    medical_record = MedicalRecords.query.get(id)
    if not medical_record:
        return jsonify({'message': 'Medical record not found'}), 404
    return jsonify(medical_record.serialize()), 200

@medical_record_bp.route('/<int:id>', methods=['PUT'])
def update_medical_record(id):
    data = request.get_json()
    medical_record = MedicalRecords.query.get(id)
    if not medical_record:
        return jsonify({'message': 'Medical record not found'}), 404
    for key, value in data.items():
        setattr(medical_record, key, value)
    db.session.commit()
    return jsonify(medical_record.serialize()), 200

@medical_record_bp.route('/<int:id>', methods=['DELETE'])
def delete_medical_record(id):
    medical_record = MedicalRecords.query.get(id)
    if not medical_record:
        return jsonify({'message': 'Medical record not found'}), 404
    db.session.delete(medical_record)
    db.session.commit()
    return jsonify({'message': 'Medical record deleted'}), 200
