import sys
def qq():
    print('qq')
     
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
var = 'privet'
__qwe__ = 'qwe'
print(dir(sys))
print(dir())