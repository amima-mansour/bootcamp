import sys


def usage():
    print('Usage: python operations.py\nExample:\npython operations.py 10 3')
    sys.exit()


def operations(a, b):
    try:
        a = int(a)
        b = int(b)
        print('Sum: ', a + b)
        print('Difference: ', a - b)
        print('Product: ', a * b)
        if b == 0:
            print('Quotient: ERROR (div by zero)')
            print('Remainder: ERROR (modulo by zero)')
        else:
            print('Quotient: ', a / b)
            print('Remainder: ', a % b)
    except ValueError:
        print('InputError: only numbers')
        usage()


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print('InputError: too many arguments')
        usage()
    if len(sys.argv) < 3:
        usage()
    operations(sys.argv[1], sys.argv[2])
