from flask import Blueprint, request, jsonify
from app import db
from app.models import Monitor
from flask import render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/monitors', methods=['POST'])
def add_monitor():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    monitor = Monitor(url=url)

    db.session.add(monitor)
    db.session.commit()

    return jsonify({
        "message": "Monitor added successfully",
        "monitor": monitor.to_dict()
    }), 201


@main.route('/api/monitors', methods=['GET'])
def get_monitors():
    monitors = Monitor.query.all()
    return jsonify([m.to_dict() for m in monitors]), 200

@main.route('/api/monitors/<int:id>', methods=['DELETE'])
def delete_monitor(id):
    monitor = Monitor.query.get(id)

    if not monitor:
        return jsonify({"error": "Monitor not found"}), 404

    db.session.delete(monitor)
    db.session.commit()

    return jsonify({"message": "Monitor deleted"}), 200