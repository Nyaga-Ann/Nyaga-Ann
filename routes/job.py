from flask import Blueprint, request, jsonify
from models import db, Job

job_bp = Blueprint('job_bp', __name__)

@job_bp.route('/', methods=['POST'])
def create_job():
    data = request.get_json()
    new_job = Job(**data)
    db.session.add(new_job)
    db.session.commit()
    return jsonify(new_job.serialize()), 201

@job_bp.route('/', methods=['GET'])
def get_all_jobs():
    jobs = Job.query.all()
    return jsonify([job.serialize() for job in jobs]), 200

@job_bp.route('/<int:id>', methods=['GET'])
def get_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({'message': 'Job not found'}), 404
    return jsonify(job.serialize()), 200

@job_bp.route('/<int:id>', methods=['PUT'])
def update_job(id):
    data = request.get_json()
    job = Job.query.get(id)
    if not job:
        return jsonify({'message': 'Job not found'}), 404
    for key, value in data.items():
        setattr(job, key, value)
    db.session.commit()
    return jsonify(job.serialize()), 200

@job_bp.route('/<int:id>', methods=['DELETE'])
def delete_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({'message': 'Job not found'}), 404
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted'}), 200
