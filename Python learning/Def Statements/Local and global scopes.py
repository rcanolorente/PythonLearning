def spam():
    eggs = 99
    bacon()
    print(eggs, "two")

def bacon():
    ham = 101
    eggs = 0
    print(eggs, "one")

spam()

#When bacon() returns, the local scope for that call is destroyed. The program execution continues
# in the spam() function to print the value of eggs ❸, and since the local scope for the call to spam()
# still exists here, the eggs variable is set to 99. This is what the program prints.