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


def ft_zoom(img):
    """_summary_
    catch only 400x400 pixels of the image

    Args:
        img (array): numpy array of image

    Returns:
        None
    """
    # definition of the zoom area
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
    print(img_zoomed)
    plt.imshow(img_zoomed, cmap="gray")
    plt.show()
    plt.close()


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
    ft_zoom(img_for_zoom)


if __name__ == "__main__":
    main()
