from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 2083 is a common max URL length
    url = db.Column(db.String(2083), nullable=False)
    # Stores the QR image binary data
    qr_image = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<QRCode {self.url}>"
