MIN_LEN = 5


def main():
    password = get_password()

    convert_password(password)


def convert_password(password):
    print(len(password) * '*')


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MIN_LEN:
        print("This password isn't long enough.")
        password = input("Please enter your password: ")
    return password


main()
