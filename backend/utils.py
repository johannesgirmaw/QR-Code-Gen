import re


def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)'
        r'((([A-Za-z0-9-]+\.)+[A-Za-z]{2,})|'
        r'localhost|'
        r'(\d{1,3}\.){3}\d{1,3})'
        r'(:\d+)?'
        r'(\/\S*)?$', re.IGNORECASE)
    return re.match(regex, url) is not None
