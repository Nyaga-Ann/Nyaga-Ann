from flask import Blueprint, request, jsonify
from models import db, Training

training_bp = Blueprint('training_bp', __name__)

@training_bp.route('/', methods=['POST'])
def create_training():
    data = request.get_json()
    new_training = Training(**data)
    db.session.add(new_training)
    db.session.commit()
    return jsonify(new_training.serialize()), 201

@training_bp.route('/', methods=['GET'])
def get_all_trainings():
    trainings = Training.query.all()
    return jsonify([training.serialize() for training in trainings]), 200

@training_bp.route('/<int:id>', methods=['GET'])
def get_training(id):
    training = Training.query.get(id)
    if not training:
        return jsonify({'message': 'Training not found'}), 404
    return jsonify(training.serialize()), 200

@training_bp.route('/<int:id>', methods=['PUT'])
def update_training(id):
    data = request.get_json()
    training = Training.query.get(id)
    if not training:
        return jsonify({'message': 'Training not found'}), 404
    for key, value in data.items():
        setattr(training, key, value)
    db.session.commit()
    return jsonify(training.serialize()), 200

@training_bp.route('/<int:id>', methods=['DELETE'])
def delete_training(id):
    training = Training.query.get(id)
    if not training:
        return jsonify({'message': 'Training not found'}), 404
    db.session.delete(training)
    db.session.commit()
    return jsonify({'message': 'Training deleted'}), 200
