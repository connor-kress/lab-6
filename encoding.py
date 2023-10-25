"""Written by Connor Kress."""


def print_menu() -> None:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')


def get_input() -> int:
    return int(input('Please enter an option: '))


def encode(string: str) -> str:
    return ''.join(str((int(c)+3) % 10) for c in string)


# def decode(string: str) -> str:
#     return ''.join(str((int(c)-3) % 10) for c in string)


def main() -> None:
    password = None
    while True:
        print_menu()
        match get_input():
            case 1:
                string = input('Please enter your password to encode: ')
                password = encode(string)
                print('Your password has been encoded and stored!')
            case 2:
                if password is None:
                    raise Exception('No password yet.')
                print(f'The encoded password is {password}, and the '
                      f'original password is {decode(password)}.')
            case 3:
                break
        print()


if __name__ == '__main__':
    main()
