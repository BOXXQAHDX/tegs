#модуль для работы с интерфэйсом


def menu (punct:list, top:int):
    '''функция для создания меню'''
    for x in range (len (punct)):   
        if top == x:
            print (punct[x],'<')
        else:
            print (punct[x])

