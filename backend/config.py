import os


class Config:
    # Use an environment variable for the database URL; fallback to a default
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'postgresql://nisir:nisir@localhost/qr_generator;'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
