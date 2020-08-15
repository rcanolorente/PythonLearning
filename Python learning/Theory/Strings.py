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
#istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.





print('How are you?')
feeling = input()
if feeling.lower() == 'great':  # it does not matter whether the user types Great, GREAT, or grEAT,
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

