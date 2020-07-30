animals =['cat', 'bat', 'rat', 'elephant']
print(animals)
print(animals[0] )
spam = [['cat', 'bat'], [1,2,3,4]] #list of lsits
print(spam)
print(spam[1])
print(spam[1][3])#grabs the 4th value in the second list

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1]) #negative index refer to the last item
print(spam[-3])

print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.' 'The elephant is afraid of the bat.')
print(spam[1:3]) #A slice goes up to, but will not include, the value at the second index.['bat', 'rat']

#As a shortcut, you can leave out one or both of the indexes on either side of the colon in the slice.
print(spam[:2])
print(spam[1:])
print(spam[:])
print(len(spam))#len returns the number of items ona list

spam[1]='hello'
print(spam[:])
del spam[2]  #delete one
print(spam[:])