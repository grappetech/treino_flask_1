import base64
import socket
import string

from flask_bcrypt import Bcrypt

from erp.models.entity import Entity


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


def as_dict(model):
    result_dict = {}
    for attr in vars(model):
        attr_value = getattr(model, attr)
        if isinstance(attr_value, Entity):
            result_dict[attr.replace('__', '')] = as_dict(attr_value)
        if isinstance(attr_value, list):
            result_dict[attr.replace('__', '')] = []
            for item in attr_value:
                result_dict[attr.replace('__', '')].append(item)
        result_dict[attr.replace('__', '')] = attr_value
    print(result_dict)
    return result_dict
