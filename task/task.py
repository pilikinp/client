import time
from .utils import act_time

status = {'waiting', 'doing', 'done'}


class Task:

    def __init__(self, creator, viewer=None, task_name=None):
        '''
        :param creator: объект класса Пользователь (?) создатель задачи
        :param viewer: объект класса Пользователь (?) кто просматривает задачу
        :param task_name: название задачи, если не установленно, то Новая задача
        '''
        self._creator = creator
        self.viewer = viewer
        self._task_name = 'Новая задача' if not task_name else task_name
        self._text = None
        self._creating_time = time.time()
        self.deadline_time = None
        self.status = 'waiting'
        self._implementors = [creator]

    def __repr__(self):
        return 'Task: {} / creator: {} / created: {} /\n' \
               'text: {} / implementers: {}'.format(self._task_name,
                                                    self._creator,
                                                    self._creating_time,
                                                    self._text,
                                                    self._implementors)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        print("Creator couldn't be set")

    @creator.getter
    def creator(self):
        return self._creator

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if self._creator != self.viewer:
            print('Only creator could set text')
        else:
            self._text = text

    def text_edit(self):
        if self._creator != self.viewer:
            print('Only creator could edit text')
        else:
            original_text = self._text
            editing = input('давайте редактировать: ')  # обрабатываем исходный текст задачи
            self._text = original_text


if __name__ == '__main__':
    task = Task(creator='Jack', viewer='Jack11', task_name='New one')
    print(task.creator)

    task.text = 'kjdhkfjhg'
    print(task.text)

    task.text_edit()

    print(task.text)
