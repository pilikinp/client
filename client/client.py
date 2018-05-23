import time, sys
import socket
import threading, queue
import hashlib

from jim.jim import JimRequest, JimResponse

class Client():
    request = JimRequest()
    response = JimResponse()

    username = ''

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.lock = threading.Lock()
        self.recv_queue = queue.Queue()
        self.secret = 'secretkey'

    @property
    def socket(self):
        return self._sock

    def connect_guest(self, name, password):
        # Функция авторизации пользователя
        self.username = name
        pas = hashlib.sha256()
        pas.update(self.username.encode())
        pas.update(password.encode())
        pas.update(self.secret.encode())
        password = pas.hexdigest()
        msg = self.run()
        if msg == 'соединение установлено':
            data = {'action': 'sign in',
                    'time': time.ctime(),
                    'data':{'user': self.username,
                    'password': password}}
            self.socket.send(self.request.pack(data))
            print('сообщение отправлено')

            msg_recv = self.socket.recv(4096)
            msg_recv = self.response.unpack(msg_recv)

            print(msg_recv)
            # if msg_recv['response'] == '102':
            #             #     print(msg_recv['data']['alert'])
            #             #     self.start_thread()

            # self.recv_queue.put(msg_recv)
        else:
            print(msg)

    def registration(self, name, password, email):
        pass

    def add_task(self):
        # функция добавления задачи
        pass


    def _get_message(self):

        #получение сообщений от сервера, пока только вывод в консоль, сервер без бд поэтому просто пересылает сообщение

        sock = self.socket
        cont_l = []
        while True:
            try:
                sock.settimeout(12)
                data_recv = sock.recv(1024)
                data_recv = JimRequest.unpack(data_recv)
                data = data_recv['data']
                print(data_recv)
            except socket.timeout:
                pass

    def start_thread(self):
        t2 = threading.Thread(target=self._get_message)
        t2.daemon = True
        t2.start()


    def run(self):
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self._host, self._port))
            return 'соединение установлено'
        except:
            return 'Сервер не отвечает'