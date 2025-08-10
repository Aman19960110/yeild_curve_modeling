#goal Obtain transform and visulize US yeild data.
#Impoting requried library
import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Using Fred API to get US yeild data
fred = Fred(api_key='a4d321de7f4380b06557a92a24a2c703')
series_ids = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', \
              'DGS7', 'DGS10', 'DGS20', 'DGS30']

def get_yield_data(series_id):
    data = fred.get_series(series_id, observation_start="1975-01-01", observation_end="2025-08-01")
    return data

yiled_dict = {series_id: get_yield_data(series_id) for series_id in series_ids}