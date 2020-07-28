def collatz (number):
    if (float(number%2)) ==0:
    #even
        print(number//2)
        return number // 2
    else:
        #uneven
        return 3 * number + 1


z= int(input('Please enter number: '))

while z != 1:
    z=collatz(int(z))

#while collatz(z) != 1:
    #z = int(input())




