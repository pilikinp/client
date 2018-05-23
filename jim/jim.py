import json
import time

class JimRequest():

    def pack(self, msg):
        '''Упаковываем сообщение'''
        data = json.dumps(msg).encode()
        return data

    def unpack(self, data):
        '''Распаковка сообщения'''
        data = json.loads(data.decode())

        return data


class JimResponse(JimRequest):
    code = {
        '100': 'Базовое уведомление',
        '101': 'Важное уведомление',
        '102': 'В сети',
        '200': 'Ок',
        '201': 'Объект создан',
        '202': 'Подтверждение',
        '400': 'Неправильный запрос/JSON-объект',
        '401': 'Не авторизован',
        '402': 'Не правильный логин/пароль',
        '403': 'Пользователь заблокирован',
        '404': 'Пользователь отсутствует',
        '409': 'Уже имеется подключение с указанным логином',
        '500': 'Ошибка сервера'
    }

    def msg(self, code, username=''):
        msg = {'response': code,
               'time': time.ctime(),
               'data':{'alert': self.code[code],
               'user': username}}
        return msg