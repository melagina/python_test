'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func('')
func(25, c=24)
func(c=50, a=100)