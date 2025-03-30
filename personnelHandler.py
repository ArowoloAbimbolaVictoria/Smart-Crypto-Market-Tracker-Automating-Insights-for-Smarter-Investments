# personnelHandler.py
import pandas as pd

def read_personnel(filename):
    """
    Reads personnel CSV file and returns a list of dictionaries 
    containing names and email addresses.
    
    :param filename: Path to the personnel CSV file.
    :return: List of dictionaries with 'Name' and 'Email' keys.
    """
    df = pd.read_csv(filename)
    return df.to_dict('records')
