spam = ['apples', 'bananas', 'tofu', 'cats']
i = -1

print((len(spam)))

def MakeList(words):
    for i in range(len(words)-2):
        print(words[i], end=',')
    print(words[-2], 'and', words[-1])
MakeList(spam)


#DO it FANCY
def commacode(passedlist):
    stringy = ''
    for i in range(len(passedlist)-1):
        stringy += str(passedlist[i]) + ', '
        # adds all except last item to str
    stringy += 'and ' + str(passedlist[-1])
    # adds last item to string, after 'and'
    print(stringy)
    return stringy


commacode(spam)