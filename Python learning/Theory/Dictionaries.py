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

#It’s tedious to check whether a key exists in a dictionary before accessing that key’s value.
# Fortunately, dictionaries have a get() method that takes two arguments:
# the key of the value to retrieve and a fallback value to return if that key does not exist.

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print( 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get() method.
# Without using get(), the code would have caused an error message, such as in the following example:

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white') #When spam.setdefault('color', 'white') is called next, t
# he value for that key is not changed to 'white' because spam already has a key named 'color'.
print(spam)

spam = { 'cat' : 'soft'}