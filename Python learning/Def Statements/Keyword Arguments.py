# Keyword arguments are often used for optional parameters. For example, the print() function has the optional
# parameters end and sep to specify what should be printed at the end of its arguments and
# between its arguments (separating them), respectively.
print('Hello', end='')
print('World')


#Similarly, when you pass multiple string values to print(),
# the function will automatically separate them with a single space.
print('cats', 'dogs', 'mice')

#But you could replace the default separating string by passing
# the sep keyword argument. Enter the following into the interactive shell:
print('cats', 'dogs', 'mice', sep=',')