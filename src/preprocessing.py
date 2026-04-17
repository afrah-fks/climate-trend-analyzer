import pandas as pd

def preprocess_data(df):
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])

    # Handle missing values
    df = df.ffill()

    # Remove duplicates
    df = df.drop_duplicates()

    return df