
# Program 1
out_file = open('name.txt', 'w')
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

# Program 2
in_file = open('name.txt', 'r')
name = in_file.read().strip()
print("Your name is {}".format(name))
in_file.close()


# Program 3
result = 0
out_file = open('numbers.txt', 'r')
for line in out_file:
    result += int(line)
print(result)
