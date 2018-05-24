import time

time_format = '%d.%m.%Y - %H:%M:%S'


def act_time(time_):
    t_local = time.localtime(time_)
    t = time.strftime(time_format, t_local)
    return t


if __name__ == '__main__':
    pass
