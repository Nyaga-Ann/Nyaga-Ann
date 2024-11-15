from flask import Blueprint, request, jsonify
from models import db, ReportManagement

report_management_bp = Blueprint('report_management_bp', __name__)

@report_management_bp.route('/', methods=['POST'])
def create_report():
    data = request.get_json()
    new_report = ReportManagement(**data)
    db.session.add(new_report)
    db.session.commit()
    return jsonify(new_report.serialize()), 201

@report_management_bp.route('/', methods=['GET'])
def get_all_reports():
    reports = ReportManagement.query.all()
    return jsonify([report.serialize() for report in reports]), 200

@report_management_bp.route('/<int:id>', methods=['GET'])
def get_report(id):
    report = ReportManagement.query.get(id)
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    return jsonify(report.serialize()), 200

@report_management_bp.route('/<int:id>', methods=['PUT'])
def update_report(id):
    data = request.get_json()
    report = ReportManagement.query.get(id)
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    for key, value in data.items():
        setattr(report, key, value)
    db.session.commit()
    return jsonify(report.serialize()), 200

@report_management_bp.route('/<int:id>', methods=['DELETE'])
def delete_report(id):
    report = ReportManagement.query.get(id)
    if not report:
        return jsonify({'message': 'Report not found'}), 404
    db.session.delete(report)
    db.session.commit()
    return jsonify({'message': 'Report deleted'}), 200
