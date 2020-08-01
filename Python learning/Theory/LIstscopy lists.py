import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

#If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
# The deepcopy() function will copy these inner lists as well.
