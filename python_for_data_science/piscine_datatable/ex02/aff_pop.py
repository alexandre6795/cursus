import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from load_csv import load


def convert_format(value,_):
    """
    Format a number into human-readable form with k, M, B.
    Args:
        value (float): Value to format.
        _ : Not used (required by FuncFormatter).
        
    Returns:
        str: Formatted string.
    """
    if (value >= 1_000_000_000):
        return f"{value/1_000_000_000:.1f}B"
    if (value >= 1_000_000):
        return f"{value/1_000_000:.1f}M"
    if (value >= 1_000):
        return f"{value/1_000:.1f}k"
    return f"{value:.0f}"
        

def convert_to_float(value)->float:
    """
    Convert a string to float.
    Args:
        value (str): string to convert to float.
        
    Returns:
        float: the converted value or None if the conversion failed.
    """
    if(type(value)==str):
        value = value.strip().lower()
        if(value[-1]=="k"):
            value = float(value[:-1])*1000
        elif(value[-1]=="m"):
            value = float(value[:-1])*1000000
        elif(value[-1]=="b"):
            value = float(value[:-1])*1000000000
        else:
            if(value.isnumeric):
                value = float(value)
            else:
                value = None
    return value
    

def display_population(data,country1,country2):
    """
    Display the population of a country over the years.
    Args:
        data (DataFrame): DataFrame containing year and population columns.
        country1 (str): name of the first country
        country2 (str): name of the second country
        
    Returns:
        None
    """
    country1_data = data[data["country"].str.contains(country1, case=False, na=False)]
    country2_data = data[data["country"].str.contains(country2, case=False, na=False)]
    if country1_data.empty or country2_data.empty:
        print(f"No data for country {country1} or {country2}")
        return
    country1_pop = country1_data.iloc[0, 1:].apply(convert_to_float)
    country2_pop = country2_data.iloc[0, 1:].apply(convert_to_float)
    years = data.columns[1:].astype(int)  # Convertir les années en entier
    
    print(f"{country1} population over the years")
    print(f"{country1_pop}")
    print(f"{country2} population over the years")
    print(f"{country2_pop}")
    
    

    # Création du graphique
    plt.plot(years, country1_pop, color='b') # Création du graphique avec la couleur bleue
    plt.plot(years, country2_pop, color='r') # Création du graphique avec la couleur rouge
    plt.title(f"Population Projections")
    plt.xlabel("Year") # ajout d'un titre à l'axe des abscisses
    plt.ylabel("Population") #ajout d'un titre à l'axe des ordonnées
    # plt.grid(True) ajout d'une grille

    # Affichage de l'axe X avec un pas de 10 ans
    step = 40
    ymin = min(min(country1_pop),min(country2_pop))
    ymax = max(max(country1_pop),max(country2_pop))
    ystep = (max(int((ymax-ymin)/10),1))
    plt.yticks(range(int(ymin), int(ymax) + 1, ystep))
    plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(convert_format))
    plt.xticks(range(min(years), max(years), step)) # xticks permet de définir les valeurs de l'axe des abscisses
    step = 10
    # plt.ticklabel_format(style="plain", axis="y")
    plt.legend([country1, country2], loc='lower right') # ajout d'une légende
    # si tu veux que cela soit plus lisible tu peux mettre un pas de 10 ans et une rotation de 45°
    plt.xticks(range(min(years), max(years), step),rotation=45) # xticks permet de définir les valeurs de l'axe des abscisses
    plt.tight_layout() # ajustement automatique des marges pour éviter que les labels ne soient coupés

    plt.show()
    return
    
def main():
    """
    Take two countries as argument and display the population of these countries over the years
    ex : python aff_pop.py France Belgium
    if country is not given, the population France over the years
    because i'm french
    and diplay Belgium population too because it's the subject example
    """
    print("coucou")
    if len(sys.argv) != 3:
        country1 = "France"
        country2 = "Belgium"
    else:
        country1 = sys.argv[1].strip()
        country2 = sys.argv[2].strip()
    df = load("population_total.csv")
    display_population(df, country1, country2)
    return

if __name__ == "__main__":
    main()
        
        