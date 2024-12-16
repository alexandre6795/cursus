# slice est une méthode qui permet de découper une liste en fonction
# - de l'index de début et de fin
# ex : liste = [1,2,3,4,5,6,7,8,9,10]
# liste[0:2] => [1,2]
# un index négatif permet de partir de la fin de la liste
# liste[1:-2] => [2,3,4,5,6,7,8]
# tout les index peuvent etre négatif
# liste[-2:] => [9,10]
# un index peut depasser la taille de la liste start et end
# liste[1:100] => [2,3,4,5,6,7,8,9,10]
# liste[-100:-2] => [1,2,3,4,5,6,7,8]
# en gros liste[<=start > end]
# un troisième argument permet de définir le pas
# liste[1:10:2] => [2,4,6,8,10]

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a list of lists and two integers as arguments.
    It returns a new list of lists that contains the
    elements of the original list(<=start > end).
    usage: slice_me([list],start,end).
    """
    try:
        if type(family) is not list:
            raise TypeError("You must enter a list")
        if (any(type(x) is not list for x in family) or len(family) == 0):
            raise TypeError("You must enter a list of lists")
        if (isinstance(start, int) is False or isinstance(end, int) is False):
            raise ValueError("You must enter an integer")
        if any(len(x) != len(family[0]) for x in family):
            raise ValueError("All lists must have the same length")
        print(f"My shape is : {len(family), len(family[0])}")
        newnp = np.array(family[start:end])
        print(f"My new shape is : {len(newnp), len(newnp[0])}")
    except (ValueError, TypeError) as e:
        print(e)
        exit()

    return (newnp.tolist())

# from array2D import slice_me
# family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
# result
#  python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
