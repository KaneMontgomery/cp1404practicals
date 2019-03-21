"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""Value error will occur when either the numerator or denominator are not numbers and are instead letters or symbols"""
"""Zero division error will occur if the denominator is inputted as 0"""
"""You could change the code to avoid the possibility of a zero division error by adding a while loop to check if
the denominator is greater than 0 and if it isn't, that it isn't a valid number"""
