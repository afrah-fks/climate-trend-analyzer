import pandas as pd
import numpy as np
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create correct path
file_path = os.path.join(BASE_DIR, "data", "raw", "climate_data.csv")

# Generate data
dates = pd.date_range(start="2010-01-01", periods=1000)

data = pd.DataFrame({
    "Date": dates,
    "Temperature": np.random.normal(25, 5, len(dates)),
    "Rainfall": np.random.normal(100, 20, len(dates))
})

# Save file
data.to_csv(file_path, index=False)

print("Dataset saved at:", file_path)