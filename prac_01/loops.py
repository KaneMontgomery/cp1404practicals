n = int(input("Please enter a number: "))
if n <= 0:
    print('That is not a valid number.')

for i in range(1, 21, 2):
    print(i, end='')
print()

for i in range(0, 101, 10):
    print(i, end='')
print()

for i in range(20, 0, -1):
    print(i, end='')
print()

for i in range(0, n, 1):
    print("*", end='')
print()

for i in range(1, n + 1, 1):
    print("*" * i)
print()
