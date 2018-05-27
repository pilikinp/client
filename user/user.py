from base.base import FieldType


class User:
    '''
    основные поля name и password, вся дополнительная информация в info в виде словаря
    '''

    name = FieldType('name', '', str)
    password = FieldType('password', '', str)
    info = FieldType('info', dict(), dict)

    __slots__ = {name.name, password.name, info.name}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def user_dict(self):
        _dict = dict()
        for key in self.__slots__:
            try:
                value = getattr(self, key)
                _dict[key.lstrip('_')] = value
            except AttributeError:
                pass
        return _dict


if __name__ == '__main__':
    pass
