from app import db

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default="UNKNOWN")

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "status": self.status
        }