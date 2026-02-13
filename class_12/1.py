import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    if path.endwith(".csv"):
        return pd.read_csv
    
def inspect(df):
    
