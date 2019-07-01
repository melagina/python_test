'''
Created on 21 июн. 2019 г.

@author: m.elagina
'''
try:
    s = input('Enter something --> ')
    Print(s)
except NameError as ex:
    print(ex.length)
else:    
    print("else")
finally:
    print('(Cleaning up: Closed the file)')    