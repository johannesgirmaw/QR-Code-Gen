
from flask import Flask, request, jsonify
import qrcode
import io
import re
import base64
from models import QRCode
from db import db


def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)'
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,})|'
        r'localhost|'
        r'(\d{1,3}\.){3}\d{1,3})'
        r'(:\d+)?'
        r'(\/\S*)?$', re.IGNORECASE)
    return re.match(regex, url) is not None


@app.route('/api/generate_qr', methods=['POST'])
def generate_qr():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'Missing URL in request'}), 400

    url = data['url']
    if not is_valid_url(url):
        return jsonify({'error': 'Invalid URL provided'}), 400

    # Generate the QR code
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

    # Optionally, store the record in the database
    qr_record = QRCode(url=url, qr_image=img_data)
    db.session.add(qr_record)
    db.session.commit()

    # Return the image as a Base64 encoded string
    img_base64 = base64.b64encode(img_data).decode('utf-8')
    return jsonify({'qr_code': img_base64})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
