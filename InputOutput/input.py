'''
Created on 20 июн. 2019 г.

@author: m.elagina
'''
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input('enter text: ')
if (is_palindrome(something)):
    print("yes, it's palindrome")
else:
    print("No, it's not a palindrome")