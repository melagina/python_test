'''
Created on 30 мая 2019 г.

@author: m.elagina
'''
def total(initial=5, *numbers, **keywords):
    count = initial
    print('count = ', count)
    for number in numbers:
        count += number
        print('count = ', count)
        print('number = ', number)
        print('numbers = ', numbers)
    for key in keywords:
        count += keywords[key]
        print('count = ', count)
        print('key = ', key, 'value = ', keywords[key])
        print('keywords = ', keywords)
    return count
print(total(10, 1, 2, 3, qq=50, fruits=100))