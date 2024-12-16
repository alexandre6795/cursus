import sys

morse_code = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
              "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
              "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
              "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
              "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
              "2": "..---",  "3": "...--", "4": "....-", "5": ".....",
              "6": "-....", "7": "--...", "8": "---..", "9": "----."}


def ft_apply(fct, iterable):
    """
    apply a function to the elements of an iterable
    """
    return (fct(item) for item in iterable)


def ft_morse(x):
    """"
    converts a character into Morse code
    """
    return (morse_code[x.upper()]+" ")


def ft_check(x):
    """
    checks if the string contains only alpha or numeric or space characters
    """
    return (any(not (c.isalnum() or c.isspace())for c in x))


def main():
    """
    takes a string as an argument and encodes it into Morse Code.
    usage : python3 sos.py [word]
    """
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("only one argument is accepted")
        elif (ft_check(sys.argv[1])):
            raise AssertionError("only number or characters")
        else:
            word = sys.argv[1]
            morse = ft_apply(ft_morse, word) 
        print("".join(morse))
    except AssertionError as e:
        print("AssertionError:", e)
        return (1)


if (__name__ == '__main__'):
    main()
