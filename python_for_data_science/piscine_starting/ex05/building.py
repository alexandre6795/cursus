import sys


def uppernb(text):
    """
    return the number of upper letters in the text
    """
    return sum(1 for c in text if c.isupper())


def lowernb(text):
    """
    return the number of lower letters in the text
    """
    return sum(1 for c in text if c.islower())


def puncnb(text):
    """
    return the number of punctuation marks in the text
    """
    return sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")


def spacenb(text):
    """
    return the number of spaces in the text
    """
    return sum(1 for c in text if c.isspace() or c == "\n")


def dignb(text):
    """
    return the number of digits in the text
    """
    return sum(1 for c in text if c.isdigit())


def main():
    """
    this program take a text as argument and print
    - total number of characters
    - number of upper letters
    - number of lower letters
    - number of punctuation marks
    - number of spaces(include /n)
    - number of digits
    usage: python3 building.py [text]
    or python3 building.py
    "What is the text to count?"
    [text]
    """

    try:
        if (len(sys.argv) > 2):
            raise AssertionError("AssertionError: Wrong number of arguments")
        elif (len(sys.argv) == 1):
            print("What is the text to count?")
            text = sys.stdin.readline()
            print()
        else:
            text = sys.argv[1]
        print("The text contains", len(text), "characters:")
        print(f"{uppernb(text)} upper letters")
        print(f"{lowernb(text)} lower letters")
        print(f"{puncnb(text)} punctuation marks")
        print(f"{spacenb(text)} spaces")
        print(f"{dignb(text)} digits")
    except AssertionError as e:
        print(e)
        return 1


if __name__ == "__main__":
    main()
    