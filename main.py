#Будильник
import datetime

def setup_timer():

    print('Установите время пробуждения: ')

    while True:
        print('Часы: ')
        hours = input()
        if int(hours) <= 23 and int(hours) >= 0:
            break
        else:
            continue

    while True:
        print('Минуты: ')
        minutes = input()
        if int(minutes) <= 59 and int(minutes) >= 0:
            break
        else:
            continue

    if int(hours) < 10:
        hours = '0' + hours

    if int(minutes) < 10:
        minutes = '0' + minutes

    fulltime = hours + minutes

    return fulltime

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

def check_time():
    pass

def check_time_test():
    actualtime = datetime.datetime.now()
    if setup_timer() == actualtime.strftime('%H%M'):
        return True
    else:
        return False

print(check_time_test())