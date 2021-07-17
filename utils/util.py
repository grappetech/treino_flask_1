import base64
import socket
import string

from flask_bcrypt import Bcrypt


def get_ip():
    return [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
            [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]


def as_base64(content: string):
    message_bytes = content.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def as_password(password: string):
    return Bcrypt().generate_password_hash(password)
