#Будильник


def setup_timer():
    pass

def setup_timer_test():

    print('Установите время пробуждения: ')

    print('Часы: ')
    hours = 12
    print(hours)

    print('Минуты: ')
    minutes = 30
    print(minutes)

    fulltime = str(hours) + str(minutes)

    return fulltime

print(setup_timer_test())