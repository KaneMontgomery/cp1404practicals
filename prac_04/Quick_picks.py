import random

NUMBERS_PER_LINE = 6
MIN_NUM = 1
MAX_NUM = 45


def main():
    quick_picks = int(input("How many quick picks would you like?: "))
    while quick_picks < 0:
        print("That is an invalid number of quick picks.")
        quick_picks = int(input("Please enter a valid number of quick picks: "))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUM, MAX_NUM)
            while number in quick_pick:
                number = random.randint(MIN_NUM, MAX_NUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
