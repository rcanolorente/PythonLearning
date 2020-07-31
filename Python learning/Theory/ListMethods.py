spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam.insert(1, 'chicken')
print(spam)

spam.remove('bat') #removes the first instance of this value in the list, regardless of where it is.
print(spam)

del spam[0] #removes the alue stored in that index
print(spam)


#sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.
# his means uppercase letters come before lowercase letters.
# Therefore, the lowercase a is sorted so that it comes after the uppercase Z.

spam = [2, 5, 3.14, 1, -7]
spam.sort()#sorts out numbers and strings, as long as the list is not a mix of both
print(spam)
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)#sorts out numbers and strings, as long as the list is not a mix of both

spam.sort(reverse=True) #reverses order
print(spam)

#How about if you want TRUE alphabetical order?
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)


#Methods belong to a single data type. The append() and insert() methods are list methods
# and can be called only on list values, not on other values such as strings or integers.
eggs = 'hello'
eggs.append('world')
print(eggs)

