'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
#for loop
# function range
for i in range(1, 6):
    print(i)
    if i == 2:
        print('break cause i = 2')
        break
    print('i is in range and not equal 2')
#else part is optional
#it is always executed once after the for loop is over
#unless a break statement is encountered
else:
    print('The for loop is over')
    
