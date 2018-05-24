# дескриптор данных
class FieldType:

    def __init__(self, name, value, value_type=str, value_len=None):
        self.name = '_' + name
        self.value = value
        self.value_type = value_type
        self.value_len = value_len

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.value)

    def __set__(self, instance, value):
        if not isinstance(value, self.value_type):
            raise TypeError('Value must be {}'.format(self.value_type))
        if self.value_len:
            if isinstance(value, (int, float)):
                length = len(str(value))
            else:
                length = len(value)
            if length > self.value_len:
                raise ValueError('Max length must be {} symbols'.format(self.value_len))
        setattr(instance, self.name, value)


if __name__ == '__main__':
    pass
