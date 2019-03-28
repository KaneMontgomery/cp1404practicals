# 1. Numbers
count = 0
numbers = []
while count < 5:
    number = int(input("Please enter a number: "))
    numbers.append(number)
    count += 1
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the number is", sum(numbers) / len(numbers))

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username: ")
if username in usernames:
    print("Access Granted.")
else:
    print("Access Denied.")
