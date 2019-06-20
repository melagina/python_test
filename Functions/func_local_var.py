'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
x = 50
def func(x):
    print('x = ', x)
    x = 2
    print('changed, x = ', x)
    return x

def func_global_var():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
func(x)
print('x is still' , x)        
func_global_var()
print('x is still' , x)    
