cost=(float(input('how much does it cost? ')))
give=(float(input('how much do you give? ')))
change=give-cost
print(change)
reminder= change % 100
print(reminder)
