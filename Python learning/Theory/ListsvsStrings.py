#they behave the same in some aspects

name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])

print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
        print('* * * ' + i + ' * * *')

 #A list value is a mutable data type: It can have values added, removed, or changed.
 # However, a string is immutable: It cannot be changed

name = 'Zophie a cat'
name[7] = 'the'
print(name[7])
#Mutable versus immutable types may seem like a meaningless distinction, but Passing References will explain
# the different behavior when calling functions with mutable arguments versus immutable arguments.