for i in range(4):
    print(i)

for i in [0, 1, 2, 3]: #ranges behave like lists
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

#we can also write this instead:
size, color, disposition = cat   #The number of variables and the length of the list must be exactly equal, or
                                    # Python will give you a ValueError
print(disposition)

#The multiple assignment trick can also be used to swap the values in two variables:
a, b = 'Alice', 'Bob'
a, b = b, a

#Augmented Assignment Operators
spam = 42
spam = spam + 1
print(spam)

spam = 42
spam += 1
print(spam)

#The += operator can also do string and list concatenation,
# and the *= operator can do string and list replication. :

spam = 'Hello'
spam += ' world!'
print(spam)

bacon = ['Zophie']
bacon *= 3
print(bacon)
