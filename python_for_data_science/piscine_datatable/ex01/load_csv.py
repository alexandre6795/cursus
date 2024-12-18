import pandas as pd
import os
import sys

def load(path: str)-> pd.DataFrame:
    """
    take a csv file as argument and return the content of the file

    Args:
        path (str): path to csv file

    Returns:
        dataframe: pandas dataframe of csv file
    
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions{data.shape}")
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
    except pd.errors.EmptyDataError:
        print(f"File {path} is empty")
    except pd.errors.ParserError:
        print(f"File {path} is not a csv file")
    except Exception:
        print(f"An error occured while tryr to reading file {path}")
    return None
        