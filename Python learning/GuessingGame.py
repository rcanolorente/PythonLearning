from random import randint
n=randint(0,20)
print(n)
textguess=(input('Guess the number. you have 3 tries: '))
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
        exit()
    else:
        print('somethign went wrong!')
        exit()



if n == Guess:
    print('Got it! Good jobSconc')