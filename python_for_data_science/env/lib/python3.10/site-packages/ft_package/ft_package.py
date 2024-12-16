# pour cree un package pyton
# fichier a avoir setup,py et init.py , readme.md et license
# readme.md est un fichier qui explique le contenu du package
# license est le fichier de license qui permet de proteger le package et
# - les droits de l'auteur et des utilisateurs

# init.py est un fichier qui permet de le definir comme un package python
# - il peut etre vide ou contenir des fonctions/classes qui seront importées
# - ex: avec __all__ = ["fonction1","fct2"] permet d'importer les fonctions
# - fonction1 et fonction2 seront importées si on utilise from package import *

# setup.py est le fichier qui permet de creer le package
# - il contient les informations sur le package grace a ses arguments
# - name, version, description, url, author, author_email, license ...

# pour creer un package python il faut installer setuptools et wheel
# - pip install setuptools wheel

# pour creer le package il faut lancer la commande suivante
# - python3 setup.py sdist bdist_wheel cela va creer un dossier dist
# - dans lequel se trouve le package avec l'extension .tar.gz et .whl

# pour installer le package il faut lancer la commande suivante
# - pip install dist/nom_du_package-0.0.1.tar.gz  ou .whl

# si il y a une MAJ il faut changer la version dans le fichier setup.py
# - et relancer la commande python3 setup.py sdist bdist_wheel

# pour la mise en ligne du package il faut creer un compte sur pypi.org
# - et installer twine avec la commande pip install twine

# pour la mise en ligne il faut d-abord tester le package avec TestPyPI
# - qui est un environnement pour tester le processus de publication
# - pour cela il faut lancer la commande suivante
# - twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# si tout est bon il faut alors lancer la commande suivante
# twine upload dist/*


def count_in_list(lst, item):
    """
    takes a list and an item as arguments
    and returns the number of times the item
    appears in the list
    """
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count
