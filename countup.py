from time import sleep
from os import system, name
import keyboard

count = []
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def countup():
    while True:
        global count
        clear()
        count += 1

        print(count)
        print("press q to quit")
        sleep(.1)
        if keyboard.is_pressed('q'):
            print("CountUp will exit")
            f = open("count.txt", "w")
            f.write(str(count))
            f.close()
            sleep(3)
            break
        else:
            pass



g = open('count.txt', 'r')
count = g.readlines()
g.close()
count = int(count[0])
countup()
