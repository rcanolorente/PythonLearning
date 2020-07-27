from random import randint
import sys

n=randint(1,20)
print(n)
textguess=(input('I am thinking of a number between 1 and 20. you have 3 tries: '))
Guess=int(textguess)
print(Guess)


for count in range (1,3):
    if Guess > n:
        print('less')
        Guess = int(input('That\'s not it. Try Again: '))
    elif Guess<n:
        print('more')
        Guess = int(input('That\'s not it. Try Again: '))
    else:
        print('somethign went wrong!')
        sys.exit()


if n == Guess:
    print('Got it! Good job')
else:
    print('Nope. You lost. I was thinking of ', n)



