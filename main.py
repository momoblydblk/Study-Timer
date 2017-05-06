import time
from avalon import avalon
import configparser
import pip
pip.main(['install','plyer'])
from plyer import notification

def checkconfig(setname):
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.json')
    if setname in config == True:
        strstime = config[setname]
        stime = int(strstime)
        return stime
    else:
        return False

def nums(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def getstudytime():
    time = avalon.gets('How many minutes in an hour would you like to study?')
    time = nums(time)
    if time == False:
        avalon.error('Invalid Number!')
    elif time < 0:
        avalon.error('Invalid Number!')
    elif time > 55:
        avalon.error('Try a shorter number, you don\' t want to study that hard')
    else:
        time = time * 60
        return time

def newset(sname):
    stime = getstudytime()
    strstime = str(stime)
    config = configparser.ConfigParser()
    config[sname] = {}
    newconfig = config[sname]
    newconfig['studyhour'] = strstime
    with open('config.json','w') as configfile:
        config.write(configfile)
    readytostudy(sname,stime)

def readytostudy(name,time):
    avalon.info('Hi. %s\'s configuation has already been loaded.' % name)
    ready = avalon.ask('Are you ready to start?')
    if ready == False:
        exit
    else:
        study(time)

def study(studytime):
    while studytime:
        showtime = studytime / 60
        avalon.info('Started. I\'ll remind you to rest in %i mins.' % showtime)
        notimess = 'You have studied %i mins, take a break!' % showtime
        resttime = 60 - studytime
        time.sleep(studytime)
        notification.notify(
            title='Time to rest!',
            message=notimess,
            app_name='Study-Timer'
            )
        time.sleep(resttime)
        notification.notify(
            title='Time to rstartest!',
            message='Time to return to study, keep moving!',
            app_name='Study-Timer'
            )


name = avalon.gets("Can I have the name of your setting?")
resultcheckconfig = checkconfig(name)
if resultcheckconfig == False:
    newset(name)
else:
    readytostudy(name,resultcheckconfig)