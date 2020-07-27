
# abs(number)
#number : Can be integer, a floating point number or a complex number

# floating point number
float = -54.26
print('Absolute value of float is:', abs(float))

# An integer
int = -94
print('Absolute value of integer is:', abs(int))

# A complex number
complex = (3 - 4j)
print('Absolute value or Magnitude of complex is:', abs(complex))

#useful when calculating for example, the difference in months between two dates,
#but we don't know which date is first and which date is second,
#so we just turn the number positive.
print('')

#round(number, number of digits)
# when the (ndigit+1)th digit is =5
print(round(2.665, 2))

# when the (ndigit+1)th digit is >=5
print(round(2.676, 2))

# when the (ndigit+1)th digit is <5
print(round(2.673, 2))

