'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
while True:
    s = input('Enter smth: ')
    if s == 'quit':
        print('end!')
        break
    # built-in len function
    if len(s) < 3:
        print('Too small')
        continue
    print ('Input is of sufficient length')