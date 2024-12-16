# PIL(Python Imaging Library) ou Pillow est une librairie qui
# - permet de manipuler des images en Python.

import numpy as np
from PIL import Image
import os


def ft_load(path: str):
    """_summary_

    Args:
        path (str): path to image

    Returns:
        array: numpy array of image
    """
    try:
        if not isinstance(path, str):
            raise ValueError("You must enter a string")
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise ValueError("You must enter a jpg or jpeg file")
        if not os.path.exists(path):
            raise ValueError("The file does not exist")
        img = np.array(Image.open(path))
    except (ValueError, IOError) as e:
        print(e)
        exit()
    print(f"The shape of image is: {img.shape}")
    # le resultat de shape est un  tulpe de 3 nombres
    # le premier nombre est la hauteur de l'image
    # le deuxieme nombre est la largeur de l'image
    # le troisieme nombre est le nombre de canaux de couleur
    # - (ex : 1 pour les images en noir et blanc, 3 pour les images en couleur
    # - 4 pour les images en couleur avec canal alpha( transparence))
    return img
