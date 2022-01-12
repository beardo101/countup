from time import sleep
from os import system, name

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
        f = open("count.txt", "w")
        f.write(str(count))
        f.close()
        print(count)
        sleep(.1)



g = open('count.txt', 'r')
count = g.readlines()
g.close()
count = int(count[0])
countup()
