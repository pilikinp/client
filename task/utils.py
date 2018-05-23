import time

def act_time(time_):
    t_local = time.localtime(time_)
    t = time.strftime('%d.%m.%Y - %H:%M:%S', t_local)
    return t