#tegs

import os
import subprocess   

def rm (file):
    subprocess.call(['rm','-rf',file]) 
    print ('файл',file,'удалён')
     
def mkdir (name):
    subprocess.call(['mkdir' ,name])  

def cd (dir = '..'):
    os.chdir (dir)
    
def cd1 ():
    subprocess.call(['cd','-'])
         
def python (file):
    subprocess.call (['python',file])
                                                
def bash (file):
    subprocess.call (['bash',file])      

def vim (file):
    subprocess.call (['vim',file])

def nano (file):                            
    subprocess.call(['nano',file])

def cp (flie1, file2):
    subprocess.call(['cp','-r',file1,file2])

def mv (file1, file2):                          subprocess.call(['mv',file1,file2])

def ls ():
    x = os.listdir()
    return x

def clear ():
    subprocess.call(['clear'])
    

