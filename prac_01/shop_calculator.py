items = int(input("Please input number of items: "))
total = 0
if items <= 0:
    print("Invalid number")
    items = int(input("Please input number of items: "))
for i in range(0, items, 1):
    price = float(input("Please enter price of item: "))
    print("Price of item: {:.2f}".format(price))
    total += price
    if total > 100:
        discount = total * 0.1
        final = total - discount
    else:
        final = total
print("Total price for {:.0f}".format(items), "is {:.2f}".format(final))
print()
