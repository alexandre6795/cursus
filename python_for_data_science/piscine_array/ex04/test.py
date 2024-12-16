import numpy as np
import matplotlib.pyplot as plt

def create_matrix_10x10():
    # Crée une matrice 10x10 avec des nombres de 0 à 99
    return np.arange(100).reshape(10, 10)

def display_matrix_with_values(matrix, ax, title):
    """Affiche une matrice avec ses valeurs"""
    ax.matshow(matrix, cmap='Blues')  # Utilise une colormap mais les valeurs seront affichées
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, str(matrix[i, j]), ha='center', va='center', color='black')  # Affiche les valeurs
    ax.set_title(title)
    ax.axis('off')  # Enlève les axes pour mieux voir les valeurs

def test_matrice(matrix):
    # Créer une figure pour les sous-plots
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    # Affiche la matrice originale avec ses valeurs
    display_matrix_with_values(matrix, axes[0, 0], "Original")

    # Affiche la transposée de la matrice avec ses valeurs
    matrix_transpose = matrix.T
    display_matrix_with_values(matrix_transpose, axes[0, 1], "Transpose")

    # Affiche la rotation de 90 degrés de la matrice avec ses valeurs
    matrix_rot_90 = np.rot90(matrix, k=1)
    display_matrix_with_values(matrix_rot_90, axes[0, 2], "90° Rotation")

    # Affiche la rotation de 180 degrés de la matrice avec ses valeurs
    matrix_rot_180 = np.rot90(matrix, k=2)
    display_matrix_with_values(matrix_rot_180, axes[1, 0], "180° Rotation")

    # Affiche la rotation de 270 degrés de la matrice avec ses valeurs
    matrix_rot_270 = np.rot90(matrix, k=3)
    display_matrix_with_values(matrix_rot_270, axes[1, 1], "270° Rotation")

    # Affiche la rotation de 360 degrés de la matrice (identique à la matrice originale)
    matrix_rot_360 = matrix
    display_matrix_with_values(matrix_rot_360, axes[1, 2], "360° Rotation")

    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
matrix = create_matrix_10x10()
test_matrice(matrix)