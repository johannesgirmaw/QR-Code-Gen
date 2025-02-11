from flask import Flask, request, jsonify
from flask_migrate import Migrate
import qrcode
import io
import re
import base64

from models import db, QRCode
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)


def is_valid_url(url):
    """
    Validates the URL using a regular expression.
    """
    regex = re.compile(
        r'^(https?:\/\/)'  # Must start with http:// or https://
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,})|'  # Domain...
        r'localhost|'                          # or localhost...
        r'(\d{1,3}\.){3}\d{1,3})'              # or an IP address
        r'(:\d+)?'                            # Optional port
        r'(\/\S*)?$', re.IGNORECASE)           # Optional path
    return re.match(regex, url) is not None


@app.route('/api/generate_qr', methods=['POST'])
def generate_qr():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL in request'}), 400

    url = data['url']
    if not is_valid_url(url):
        return jsonify({'error': 'Invalid URL provided'}), 400

    # Generate QR code using the qrcode library
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to an in-memory buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    img_data = buf.getvalue()

    # Optionally, store the generated QR code in the database
    qr_record = QRCode(url=url, qr_image=img_data)
    db.session.add(qr_record)
    db.session.commit()

    # Return the QR code as a Base64 encoded string in a JSON response
    img_base64 = base64.b64encode(img_data).decode('utf-8')
    return jsonify({'qr_code': img_base64})


if __name__ == '__main__':
    app.run(debug=True)
