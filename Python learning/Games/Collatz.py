def collatz (number):
    if (float(number%2)) ==0:
    #even
        print('even')
        print(number//2)
        return number // 2
    else:
        #uneven
        print('uneven')
        result = 3 * number + 1
        print(result)
        return result

z= int(input('Please enter number: '))

while collatz(z) != 1:
    #z = int(input())
    z = int(input('Please enter number: '))


print('Well Done!')


