def add_moving_average(df):
    df['Temp_MA'] = df['Temperature'].rolling(window=30).mean()
    return df