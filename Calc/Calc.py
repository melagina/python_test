'''
Created on 27 мая 2019 г.

@author: m.elagina
'''
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.RED)
print(Back.GREEN)
print(Style.BRIGHT)
what = input("input action(+, -): ")
print(Back.CYAN)

a = float(input("input fist digit: "))
b = float(input("input second digit: "))

if what == "+":
    c = a+b    
elif what == "-":
    c = a-b
else:
    c=0        
print(Back.YELLOW)
print("result: " , c)    