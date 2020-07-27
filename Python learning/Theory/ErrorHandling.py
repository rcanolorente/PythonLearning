def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#When code in a try clause causes an error, the program execution immediately moves to the code in the except clause.
# After running that code, the execution continues as normal. The output of the previous program is as follows: