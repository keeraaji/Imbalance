from urllib import response
import requests
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta


def fetch_energinet_now_data(limit):
    """
    Fetches live power system data from the Energinet API.
    
    Parameters:
    limit (int): The number of records to fetch.

    Returns:
    dict: A JSON response containing the records.
    """
    response = requests.get(
    url=f'https://api.energidataservice.dk/dataset/ImbalancePrice?limit={limit}')
    result = response.json()

    # Extract records and convert to DataFrame
    df = pd.DataFrame(result["records"])

    # Optional: convert datetime strings to datetime objects
    df["TimeUTC"] = pd.to_datetime(df["TimeUTC"])
    df["TimeDK"] = pd.to_datetime(df["TimeDK"])
    return df


