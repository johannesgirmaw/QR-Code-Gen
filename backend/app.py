from utils import is_valid_url
from config import Config
from models import db, QRCode
import base64
import re
import io
import qrcode
from flask_migrate import Migrate
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/api/generate-qr/', methods=['POST', 'GET'])
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

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    return jsonify({'qrCode': f'data:image/png;base64,{img_str}'})


if __name__ == '__main__':
    app.run(debug=True)
