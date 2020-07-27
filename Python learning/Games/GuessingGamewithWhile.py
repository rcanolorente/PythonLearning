from random import randint
import sys

n=randint(1,20)
print(n)
textguess=(input('I am thinking of a number between 1 and 20. you have 3 tries: '))
Guess=int(textguess)
print(Guess)
count=1

while Guess != int(n):
    if Guess>n and count < 3  :
        print('less')
        Guess = int(input('That\'s not it. Try Again: '))
        count += 1
    elif Guess<n and count < 3:
        print('more')
        Guess = int(input('That\'s not it. Try Again: '))
        count += 1
    elif count == 3:
        print('That\'s not it. End of the game!')
        sys.exit()
    else:
        print('somethign went wrong!')
        sys.exit()



if n == Guess:
    print('Got it! Good jobSconc')


