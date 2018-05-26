import time
from base.utils import act_time
from comment.comment import Comment

status = {0: 'waiting', 1: 'doing', 2: 'done'}  # статус задачи, по умолчанию в ожидании


class Task:

    def __init__(self, creator, viewer=None, name=None):
        '''
        :param creator: имя Пользователя, создатель задачи
        :param viewer: имя Пользователя, кто просматривает задачу
        :param name: название задачи, если не установленно, то New task
        '''
        self._creator = creator
        self.viewer = viewer
        self._name = 'New task' if not name else name  # если задача с таким именем уже есть добавить суффикс _1(2, 3...)
        self._description = None
        self._time = time.time()
        self.deadline_time = None
        self.status = 0
        self._performer_user = [creator]  # список пользователей, которым задача сопоставленна
        self._access_users = [creator]  # список пользователе у которых есть доступ к задаче
        self._comments = dict()  # {'User_1': [{'text': text, 'time': time}, {}...], ...}

    def __repr__(self):
        return '>>>>>\nTask: {name} / creator: {creator} / created: {time} / deadline: {deadline}\n \
status: {status} / description: {description}\n \
performers: {performers} / access: {access}\n \
comments: {comments}\n>>>>>'.format(name=self._name,
                                    creator=self._creator,
                                    time=act_time(self._time),
                                    deadline=self.deadline_time,
                                    status=self.status,
                                    description=self._description,
                                    performers=self._performer_user,
                                    access=self._access_users,
                                    comments=self._comments)

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
    def description(self):
        return self._description

    @description.setter
    def description(self, text):
        if self._creator != self.viewer:
            print('<Only creator could set text>')
        else:
            self._description = text

    # TODO протестировать изменение текста в qt форме / сделать подтверждение изменения текста задачи
    def description_edit(self):
        '''
        при вызове метода подразумевается, что пользователю становится доступен текст задачи self._text, который
        сохраняется в original_text и доступен для изменения (например в каком-либо QT виджете).
        :return:
        '''
        original_description = self._description
        # обрабатываем исходный текст задачи
        edited_description = original_description + ' _and edited!'
        # переопределяем соответствующее поле
        self.description = edited_description

    # добавление исполнителя
    def add_performer(self, user):
        if user not in self._performer_user:
            self._performer_user.append(user)

    def del_performer(self, user):
        if user == self.creator:
            print('<Creator could not be removed>')
        else:
            self._performer_user.remove(user)

    def add_to_access(self, user):
        if user not in self._access_users:
            self._access_users.append(user)

    def del_from_access(self, user):
        if user == self.creator:
            print('<Creator could not be removed>')
        else:
            self._access_users.remove(user)

    def add_comment(self, comment):
        '''
        комментарии оставляют только пользователи из списка self.performer_user и self.access_users
        :param comment: словарь вида {'text': text, 'time': time, 'user': user} или экземпляр класса Comment
        :return:
        '''
        user = comment._user if isinstance(comment, Comment) else comment['user']
        text = comment._text if isinstance(comment, Comment) else comment['text']
        time = comment.time if isinstance(comment, Comment) else comment['time']
        if user in self._performer_user or user in self._access_users:
            if user in self._comments:
                self._comments[user].append({'time': time, 'text': text})
            else:
                self._comments[user] = [{'time': time, 'text': text}]
        else:
            print('You cannot leave comment here')

    def del_comment(self, comment):
        pass


if __name__ == '__main__':
    pass
