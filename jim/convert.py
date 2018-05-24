import json


DEFAULT_ENCODING = 'utf-8'


WRONG_TYPE_ERROR_TEXT = 'Wrong type.'


def bytes_to_json(request_bytes):

    if not isinstance(request_bytes, bytes):

        raise TypeError(WRONG_TYPE_ERROR_TEXT)

    request_dump = request_bytes.decode(DEFAULT_ENCODING)

    return json.loads(request_dump)


def json_to_bytes(response):

    if not isinstance(response, dict):

        raise TypeError(WRONG_TYPE_ERROR_TEXT)

    responce_dump = json.dumps(response)

    return responce_dump.encode(DEFAULT_ENCODING)