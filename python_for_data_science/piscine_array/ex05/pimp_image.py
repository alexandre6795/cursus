import matplotlib.pyplot as plt
import numpy as np

# result = array[, :, 0-> defini le rgb de la couleur rouge,
# 1-> defini le rgb de la couleur verte, 2-> defini le rgb de la couleur bleu]


def ft_invert(array) -> np.array:
    """_summary_
    take max value of the array and substract it to the array
    to invert the color of the image
    Args:
        array (array): the image to invert
    Returns:
        array: the inverted image
    """

    result = 255 - array
    plt.imshow(result)
    plt.show()
    plt.close()
    return (result)


def ft_red(array) -> np.array:
    """_summary_
    take the array and set the green and blue value to 0
    to get only the red color
    Args:
        array (_type_): _description_

    Returns:
        array: _description_
    """
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    plt.imshow(result)
    plt.title("Red")
    plt.show()
    plt.close()
    return (result)
# your code here


def ft_green(array) -> np.array:
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    plt.imshow(result)
    plt.title("Green")
    plt.show()
    plt.close()
    return (result)
# your code here


def ft_blue(array) -> np.array:
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    plt.imshow(result)
    plt.title("Blue")
    plt.show()
    plt.close()
    return (result)


def ft_grey(array) -> np.array:
    # voir recommandation  UIT-R BT709 pour la vrai conversion en gris
    #  sinon on peut faire la moyenne des 3 couleurs mais c'est moche
    result = array.copy()
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) // 3
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    # grey = (0.2126 * array[:, :, 0] +
    #         0.7152 * array[:, :, 1] +
    #         0.0722 * array[:, :, 2])
    # result[:, :, 0] = grey
    # result[:, :, 1] = grey
    # result[:, :, 2] = grey
    plt.imshow(result)
    plt.title("Grey")
    plt.show()
    plt.close()
    return (result)


__all__ = ["ft_invert", "ft_red", "ft_green", "ft_blue", "ft_grey"]
