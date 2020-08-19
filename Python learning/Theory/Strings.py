print("Hello there!\nHow are you?\nI\'m doing fine.")
print(r'hi/// & ')#raw string, backslashes areincluded.

#Multi-Line startes with triple quotes. Handy for big strings.
print('''Dear ALice, Eve's cat has been arrested for Catnapping, cat burglary, and extortion. 
Sincerely, 
Bob.''')

#you can use not in and in operators to check if a string contains a word
print('Hello' not in 'Hello World')
print('Hello' in 'Hello World')

spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())#this returns a boolean value


#isalpha() returns True if the string consists only of letters and is not blank.
#isalnum() returns True if the string consists only of letters and numbers and is not blank.
#isdecimal() returns True if the string consists only of numeric characters and is not blank.
#isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
#istitle() returns True if all the words int he string begin with an uppercase letter followed by only lowercase letters.

print('hello'.isalpha()) #True
print('hello123'.isalpha()) #False
print('hello123'.isalnum()) #True
print('hello'.isalnum()) #True
print('123'.isdecimal()) #True
print('    '.isspace()) #True
print('This Is Title Case'.istitle()) #True
print('This Is Title Case 123'.istitle()) #True
print( 'This Is not Title Case'.istitle()) #False
print('This Is NOT Title Case Either'.istitle()) #False
print('Hello world!'.startswith('Hello')) #True
print('Hello world!'.endswith('world!')) #True
print( 'abc123'.startswith('abcdef')) #False
print('abc123'.endswith('12')) #False
print('Hello world!'.startswith('Hello world!')) #True
print('Hello world!'.endswith('Hello world!')) #true

#The join() method is useful when you have a list of strings that need to be joined together
# into a single string value. The join() method is called on a string, gets passed a list
# of strings, and returns a string. The returned string is the concatenation of each string
# in the passed-in list. # For example, enter the following into the interactive shell:

print( ', '.join(['cats', 'rats', 'bats']))
print( ' '.join(['My', 'name', 'is', 'Simon']))

#Remember that join() is called on a string value and is passed a list value.
# (It’s easy to accidentally call it the other way around.) The split() method does
# the opposite: It’s called on a string value and returns a list of strings.

print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

#The rjust() and ljust() string methods return a padded version of the string they are called on,
# with spaces inserted to justify the text
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))

#An optional second argument to rjust() and ljust() will specify a fill character other than a space character.
print( 'Hello'.rjust(20, '*'))

#center
print( 'Hello'.center(20, '='))

spam = '    Hello World     '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())