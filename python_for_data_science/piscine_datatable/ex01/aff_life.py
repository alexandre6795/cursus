import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
from load_csv import load

def display_life_expectancy(data):
    """
    Display the life expectancy of a country over the years with steps of 10 years on the X-axis.
    Args:
        data (DataFrame): DataFrame containing year and life expectancy columns.
    """
    # Transformation des données : Années en colonnes et valeurs en lignes
    country_name = data["country"].values[0]
    years = data.columns[1:].astype(int)  # Convertir les années en entier
    values = data.iloc[0, 1:]  # iloc est une methode de panda qui permet de selectionner des données en fonction de leur position iloc[ligne, colonne]

    # Création du graphique
    plt.plot(years, values, color='b') # Création du graphique avec la couleur bleue
    plt.title(f"{country_name} life expectancy over the years")
    plt.xlabel("Year") # ajout d'un titre à l'axe des abscisses
    plt.ylabel("Life Expectancy") #ajout d'un titre à l'axe des ordonnées
    # plt.grid(True) ajout d'une grille

    # Affichage de l'axe X avec un pas de 10 ans
    step = 40
    plt.xticks(range(min(years), max(years), step)) # xticks permet de définir les valeurs de l'axe des abscisses
    step = 10
    #si tu veux que cela soit plus lisible tu peux mettre un pas de 10 ans et une rotation de 45°
    plt.xticks(range(min(years), max(years), step),rotation=45) # xticks permet de définir les valeurs de l'axe des abscisses
    plt.tight_layout() # ajustement automatique des marges pour éviter que les labels ne soient coupés

    plt.show()
    
def main():
    """
    Take a country as argument and display the life expectancy of this country over the years
    if country is not given, display the life expectancy of France over the years
    because i'm french
    """
    
    if len(sys.argv) != 2:
        country = "France"
    else:
        country = sys.argv[1].strip()
    df = pd.read_csv("life_expectancy_years.csv")
    country_data = df[df["country"].str.contains(country, case=False, na=False)]
    if country_data.empty:
        print(f"No data for country {country}")
        return
    #print(f"{country_data}")
    display_life_expectancy(country_data)
    return
    
    
if __name__ == "__main__":
    main()