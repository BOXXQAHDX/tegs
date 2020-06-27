#файловый мэнэджер

import myfi
import tehe

def inter (top):
    myfi.clear ()
    print ('''——————————— MYfiles ——— мои файлы ——————————''')
    dirs = myfi.ls ()
    tehe.menu (dirs, top)
    print ('''———————————————— управление ————————————————
w - верх
a - вниз
1 - открыть
2 - назад
3 - •••
———————————————————————————————————————————''')
    inpy = input (': ')
    if inpy == 'w':
        top -= 1
    elif inpy == 'a':
        top += 1
    elif inpy == '1':
        print ('''—————————————— открыть как —————————————————
1 - python
2 - bash
3 - vim
4 - nano
5 - папка       
————————————————————————————————————————————''')
        inpy = input (': ')

        if inpy == '1':
            myfi.python (dirs[top])

        elif inpy == '2':
            myfi.bash (dirs[top])

        elif inpy == '3':
            myfi.vim (dirs[top])

        elif inpy == '4':
            myfi.nano (dirs[top])

        elif inpy == '5':
            myfi.cd (dirs[top])
            top = 0

        else:
            input ('''
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       !данной команды не сушествует!↓
       !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
    elif inpy == '2':
        myfi.cd1 ()

    elif inpy == '3':
        inpy = input ('''1 - удалить
2 - создать в vim
3 - создать в nano
4 - создать папку
5 - копировать
6 - переименовать
7 - в первую папку
: ''')
        if inpy  == '1':
            myfi.rm (dirs[top])

        elif inpy == '2':
            name = input ('введите название нового файла: ')
            myfi.vim (name)

        elif inpy == '3':    
            name = input ('введите название нового файла: ')    
            myfi.nano (name)

        elif inpy == '4':    
            name = input ('введите название новой папки: ')         
            myfi.mkdir (name)

        elif inpy == '5':    
            name = input ('введите название копии файла: ')        
            myfi.cp (name)

        elif inpy == '6':            
            name = input ('введите новое название файла: ')                        
            myfi.mv (name)

        elif inpy == '7':
            myfi.cd ('..')

        else:
            input ('''      
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              !данной команды не сушествует!↓             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')

    else:
        input ('''           
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!              !данной команды не сушествует!↓             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')
    inter (top)

        
top = 0
inter (top)
