spam = ['apples', 'bananas', 'tofu', 'cats']
i = -1

print((len(spam)))

def MakeList(words):
    for i in range(len(words)-2):
        print(words[i], end=', ')
    print(words[-2], 'and', words[-1])
MakeList(spam)


def MakeList(words):
    stringy =''
    for i in range(len(words)-1):
        stringy += str(words[i]) + str(', ')

    stringy += str('and ') + str(words[-1])
    print(stringy)
MakeList(spam)

