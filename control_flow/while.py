'''
Created on 29 мая 2019 г.

@author: m.elagina
'''
number = 23
running = True

while running:
    guess = int(input('Enter integer: '))
    
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
        break #else not gonna execute
    else:
        print('No, it is a little lower than that.')
else:     
#     If there is an else clause for a while loop,
#    it is always executed unless you break out of the loop with a break statement
    print('The while loop is over.')
# Do anything else you want to do here
print('Done')

