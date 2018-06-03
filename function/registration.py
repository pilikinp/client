from client.client import send_queue
import hashlib

queue = send_queue
secret = 'secret_key'


def registration(name, password, email):
    pas = hashlib.sha256()
    pas.update(name.encode())
    pas.update(password.encode())
    pas.update(secret.encode())
    password = pas.hexdigest()
    message = {
        "head": {
            "type": "action",
            "name": "registration"
        },
        "body": {
            "name": name,
            "password": password
        }
    }
    queue.put(message)