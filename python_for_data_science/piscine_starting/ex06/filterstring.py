import sys
import ft_filter
# lambda function is used
# Les fonctions lambda sont des fonctions qui ne sont pas définies
# avec un nom, mais qui peuvent être utilisées dans des expressions
# ou des fonctions.
# Elles sont souvent utilisées dans des situations
# où une fonction simple est nécessaire
# pour une tâche spécifique, comme trier une liste ou filtrer des éléments.
# yield est un mot-clé qui est utilisé comme un return mais il retournera
# un generateur qui contiendra seulement une valeur. et reprennent l'execution
# là où elle s'était arrêtée.


def main():
    """
    this program take a list of words and an integer as arguments   
    and print the words that have more than n characters
    usage: python3 filterstring.py [word1 word2 ...] [int]
    """
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("arguments are bad")
        else:
            w = sys.argv[1].split()
            if (sys.argv[2].isdigit() is False):
                raise AssertionError("second argument must be positif int")
            n = int(sys.argv[2])
            select_words = ft_filter.ft_filter(lambda w: len(w) > n, w)
            print(tuple(select_words))
    except AssertionError as e:
        print("AssertionError:", e)
        return (1)


if (__name__ == '__main__'):
    main()
