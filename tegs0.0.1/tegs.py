
#tegs

import myfi
import tehe
import os
import subprocess

def one ():
    pass

def desk (top):
    myfi.clear ()
    menlist = ['# |система','] |MYfiles','↓ |установщик','$ |терминал']
    print ("—— tegs ————————————————————————————————————")
    tehe.menu (menlist, top)
    inpy = input ('''————————————————————————————————————————————
w - вверх
a - вниз
1 - открыть
: ''')

    if inpy == 'w':
        top -= 1

    elif inpy == 'a':
        top += 1

    elif inpy == '1':

        if top == 0:
            print ('oc -',os.name)
            print ('имя-',os.getlogin ())
            print ('''автор программы Денис Пёрлов /вк
@termux store  /телеграмм''')
            input ()

        elif top == 1:
            myfi.python ('myfiles.py')

        elif top == 2:
            us = input ('введите сылку на git директорию: ')
            print ('Хмммммммммммм. Скоро')

        elif top == 3:
            inpyt = input ('[tegs.term]/$')
            comm = inpyt.split()
            subprocess.call(comm)
            input ()
        
    else:
        input ('''
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      !данной команды несушествует!
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
               ''')
    desk (top)

top = 0
desk (top)
