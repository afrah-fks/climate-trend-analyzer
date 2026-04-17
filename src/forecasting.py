from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def forecast_temperature(df):
    df['Day'] = np.arange(len(df))

    X = df[['Day']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    # FIXED: use DataFrame instead of numpy array
    future_days = pd.DataFrame({
        "Day": range(len(df), len(df) + 30)
    })

    predictions = model.predict(future_days)

    return predictions