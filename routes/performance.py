from flask import Blueprint, request, jsonify
from models import db, Performance

performance_bp = Blueprint('performance_bp', __name__)

@performance_bp.route('/', methods=['POST'])
def create_performance():
    data = request.get_json()
    new_performance = Performance(**data)
    db.session.add(new_performance)
    db.session.commit()
    return jsonify(new_performance.serialize()), 201

@performance_bp.route('/', methods=['GET'])
def get_all_performance():
    performance_records = Performance.query.all()
    return jsonify([record.serialize() for record in performance_records]), 200

@performance_bp.route('/<int:id>', methods=['GET'])
def get_performance(id):
    performance = Performance.query.get(id)
    if not performance:
        return jsonify({'message': 'Performance record not found'}), 404
    return jsonify(performance.serialize()), 200

@performance_bp.route('/<int:id>', methods=['PUT'])
def update_performance(id):
    data = request.get_json()
    performance = Performance.query.get(id)
    if not performance:
        return jsonify({'message': 'Performance record not found'}), 404
    for key, value in data.items():
        setattr(performance, key, value)
    db.session.commit()
    return jsonify(performance.serialize()), 200

@performance_bp.route('/<int:id>', methods=['DELETE'])
def delete_performance(id):
    performance = Performance.query.get(id)
    if not performance:
        return jsonify({'message': 'Performance record not found'}), 404
    db.session.delete(performance)
    db.session.commit()
    return jsonify({'message': 'Performance record deleted'}), 200
