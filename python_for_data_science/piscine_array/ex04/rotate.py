import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load
# les fonctions de bases de matplotlib
# plot() pour dessiner un graphique par ex : plot([0,1,2,3,4],[0,1,4,9,16])
# - le premier tableau correspond aux valeurs de x
# - le deuxième tableau correspond aux valeurs de y
# show() pour afficher le graphique dessiné
# close() pour fermer la fenêtre du graphique
# imshow() pour afficher une image tirée d'un tableau numpy


def ft_transpose(img) -> np.ndarray:
    """_summary_
    transpose the image
    Args:
        img (array): numpy array of image

    Returns:
        array: numpy array of image
    """
    result = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            result[j][i] = img[i][j]
    print(f"New shape after Transpose: {result.shape}")
    return (result)


def ft_rot90(img) -> np.ndarray:
    """_summary_
    rotate the image 90 degrees
    Args:
        img (array): numpy array of image

    Returns:
        array: numpy array of image
    """
    result = np.zeros_like(img)
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            result[j][-(len(img[0])-1-i)] = img[j][i]
    return (result)


def ft_zoom(img) -> np.ndarray:
    """_summary_
    catch only 400x400 pixels of the image
    Args:
        img (array): numpy array of image

    Returns:
        None
    """
    zoom_a = {"height": 400, "width": 400, "c": 1}
    # valid of image size + zoom area size are smaller than the image
    try:
        if (img.shape[1] < 400 + zoom_a["height"]
                or img.shape[0] < 100 + zoom_a["width"]):
            raise ValueError("The image is too small to be zoomed")
    except ValueError as e:
        print(e)
        exit()
        # zooming the image
    # start image from x460 y 100 to zoom_a["height"] and zoom_a["width"]
    img_zoomed = img[100:100+zoom_a["height"],
                     460:460+zoom_a["width"], :zoom_a["c"]]

    print(f"The shape of image after zooming is: {img_zoomed.shape}", end="")
    print(f" or {img_zoomed.shape[0:2]}")
    return (img_zoomed)


def main():
    """
    _summary_
            This program will load ./animal.jpeg
        print current shape and all rgb values
        after that it will print the new shape and rgb value after zooming
        and open a window with the new zoomed image
    Args:
        None
    Returns:
        None
    """
    img_for_zoom = ft_load("./animal.jpeg")
    print(img_for_zoom)
    zoomed = ft_zoom(img_for_zoom)
    print(zoomed)
    # transpose image
    # transposer une matirce revient à échanger les lignes et les colonnes
    # [[1,2] -> [[1,3]
    # [3,4]]    [2,4]]
    transpose = ft_transpose(zoomed)
    # pour faire une rotation de 90 degres il faut maintenant echanger les
    # - valeurs de chaque colonne
    # [[1,3] -> [[2,4]
    # [2,4]]    [1,3]]
    rot90 = ft_rot90(transpose)
    print(rot90)
    plt.imshow(rot90, cmap='gray')
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()
