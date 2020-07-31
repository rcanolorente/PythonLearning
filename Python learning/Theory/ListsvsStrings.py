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

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
#Even though spam and someParameter contain separate references, they both refer to the same list.
# This is why the append('Hello') method call inside the function affects the list even after the function call has returned.


 #A list value is a mutable data type: It can have values added, removed, or changed.
 # However, a string is immutable: It cannot be changed

name = 'Zophie a cat'
name[7] = 'the'
print(name[7])
#Mutable versus immutable types may seem like a meaningless distinction, but Passing References will explain
# the different behavior when calling functions with mutable arguments versus immutable arguments.

