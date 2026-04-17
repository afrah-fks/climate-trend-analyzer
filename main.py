from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import plot_temperature
from src.trend_analysis import add_moving_average
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temperature
from src.visualize import plot_with_anomalies


def main():
    df = load_data("data/raw/climate_data.csv")

    df = preprocess_data(df)
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    processed_path = os.path.join(BASE_DIR, "data", "processed")

    os.makedirs(processed_path, exist_ok=True)
    df.to_csv("data/processed/cleaned_climate_data.csv", index=False)

    plot_temperature(df)

    df = add_moving_average(df)

    df = detect_anomalies(df)

    plot_with_anomalies(df)

    predictions = forecast_temperature(df)

    print("Next 30 days prediction:", predictions)

if __name__ == "__main__":
    main()