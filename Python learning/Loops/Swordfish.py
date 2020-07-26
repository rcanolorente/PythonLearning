while True:
    print('Who are you?')
    name= input()
    if name != 'Rosa':
        continue
    print('Hello, Rosa. What is the password? (It is a fish.)')
    password= input()
    if password == "swordfish":
        break
print('access granted')