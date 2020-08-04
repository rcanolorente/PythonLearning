spam = ['apples', 'bananas', 'tofu', 'cats']
i = -1

print((len(spam)))

spam.insert(3, 'and')
for i in range(len(spam)):
    print(spam[i], end=', ')

