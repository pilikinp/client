import time


def act_time(time_, time_format='%d.%m.%Y - %H:%M:%S'):
    '''преобразовывает время из секунд (с 01/01/1970 по настоящее время)
    в соответствии с time_format'''
    t_local = time.localtime(time_)
    t = time.strftime(time_format, t_local)
    return t


if __name__ == '__main__':
    pass
