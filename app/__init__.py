from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # SQLite DB config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitors.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app