myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print( 'My cat has ' + myCat['color'] + ' fur.')
#Unlike lists, items in dictionaries are unordered, therefore they cannot be sliced


spam = {12345: 'Luggage Combination', 42: 'The Answer'}
#Dictionaries can still use integer values as keys, just like lists use integers for indexes,
# but they do not have to start at 0 and can be any number.

#The keys(), values(), and items() Methods
spam = {'color': 'red', 'age': 42}
spam.keys()


for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

#Checking Whether a Key or Value Exists in a Dictionary
print('color' in spam.keys())

