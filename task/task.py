import time
from utils import act_time

status = {'waiting', 'doing', 'done'}  # статус задачи, по умолчанию в ожидании


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
                                                    act_time(self._creating_time),
                                                    self._text,
                                                    self._implementors)

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value=None):
        print("<Creator couldn't be set>")

    @creator.getter
    def creator(self):
        return self._creator

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if self._creator != self.viewer:
            print('<Only creator could set text>')
        else:
            self._text = text

    # TODO протестировать изменение текста в qt форме / сделать подтверждение изменения текста задачи
    def text_edit(self):
        '''
        при вызове метода подразумевается, что пользователю становится доступен текст задачи self._text, который
        сохраняется в original_text и доступен для изменения (например в каком-либо QT виджете).
        :return:
        '''
        original_text = self._text
        # обрабатываем исходный текст задачи
        edited_text = original_text + ' _and edited!'
        # переопределяем соответствующее поле
        self.text = edited_text

    def add_implementor(self, user):
        if user not in self._implementors:
            self._implementors.append(user)

    def del_implementor(self, user):
        pass


if __name__ == '__main__':
    task = Task(creator='Jack', viewer='Jack', task_name='New 11one')

    task.text = 'description of task'

    task.viewer = 'Bob'
    task.text_edit()

    print(task)
