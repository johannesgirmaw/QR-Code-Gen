from db import db


class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # URL field (max length for most URLs)
    url = db.Column(db.String(2083), nullable=False)
    # Optional: store binary image data if needed
    qr_image = db.Column(db.LargeBinary)

    def __repr__(self):
        return f"<QRCode {self.url}>"
