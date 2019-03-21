MIN_LEN = 5


def main():
    password = get_password()

    convert_password(password)


def convert_password(password):
    print(len(password) * '*')


def get_password():
    password = input("Please enter your password: ")
    if len(password) < MIN_LEN:
        password = input("Please enter your password: ")
    return password


main()
