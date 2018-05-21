from PyQt5 import QtCore

from client.client import Client

class Monitor(QtCore.QObject):

    gotData = QtCore.pyqtSignal(dict)


    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.client = Client('127.0.0.1', 7777)
        self.resv_queue = self.client.recv_queue

    def recv_msg(self):
        while 1:
            data = self.resv_queue.get()
            print(data)
            self.gotData.emit(data)