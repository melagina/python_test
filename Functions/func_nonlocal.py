'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
def func_outer():
    x = 2
    print('x is ', x)
    
    def func_inner():
        nonlocal x
        x = 5
    
    func_inner()
    print('x is ', x)
    print('changerd local x to ', x)
func_outer()
    