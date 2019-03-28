MIN_LEN = 5


def main():
    password = get_password(MIN_LEN)

    convert_password(password)


def convert_password(password):
    print(len(password) * '*')


def get_password(min_len):
    password = input("Please enter your password: ")
    while len(password) < min_len:
        print("This password isn't long enough.")
        password = input("Please enter your password: ")
    return password


main()
