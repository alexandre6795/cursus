import sys


def whatis():
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("AssertionError: Wrong number of arguments")
        elif (len(sys.argv) == 1):
            return (0)
        try:
            number = int(sys.argv[1])
            if (number % 2 == 0):
                print("Even")
            else:
                print("Odd")
        except Exception:
            raise AssertionError("AssertionError: Argument must be an integer")
    except AssertionError as e:
        print(e)
        return (1)


whatis()
