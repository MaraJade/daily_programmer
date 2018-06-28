import time
from num2words import num2words
from datetime import datetime

while True:
    current = "{:%X}".format(datetime.now())
    current = current.split(':')
    hour = num2words(int(current[0]))
    minute = num2words(int(current[1]))
    if int(current[0]) < 12:
        thing = "AM"
    else:
        thing = "PM"
    if int(current[1]) < 10:
        oh = "oh "
    else:
        oh = ""
    print ("It is " + hour + " " + oh + minute + " "+ thing)
    time.sleep(60)
