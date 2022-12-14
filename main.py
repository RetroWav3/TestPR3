#Будильник
import datetime
import pyglet

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

def check_time(buff):
    actualtime = datetime.datetime.now()
    if buff == actualtime.strftime('%H%M'):
        return True
    else:
        return False

def check_time_test():
    actualtime = datetime.datetime.now()
    if setup_timer() == actualtime.strftime('%H%M'):
        return True
    else:
        return False

def alarm():
    buff = setup_timer()

    while check_time(buff) == False:
        pass

    if check_time(buff) == True:
        mus = pyglet.resource.media('utrennijj-les.mp3')
        mus.play()

        while True:
            print('Чтобы выключить будильник напишите "1". ')
            stop = input()
            if stop == '1':
                return

def alarm_test():
    a = setup_timer()

    while check_time(a) == False:
        pass

    if check_time(a) == True:
        mus = pyglet.resource.media('utrennijj-les.mp3')
        mus.play()

        while True:
            print('Чтобы выключить будильник напишите "1". ')
            stop = input()
            if stop == '1':
                return

alarm()