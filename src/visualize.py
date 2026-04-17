import matplotlib.pyplot as plt

def plot_with_anomalies(df):
    plt.figure()
    plt.plot(df['Date'], df['Temperature'], label='Temperature')

    anomalies = df[df['Anomaly'] == 1]
    plt.scatter(anomalies['Date'], anomalies['Temperature'])

    plt.title("Anomaly Detection")
    plt.legend()
    plt.savefig("outputs/plots/anomalies.png")
    plt.close()