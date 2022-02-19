import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels


def plot_water_levels(station, dates, levels):
    """
    Task 2E by Tian Ern
    Displays a plot of the water level data against time for a station

    Args:
        station: a MonitoringStation object
        dates: list of datetime object
        levels: list of water levels in float

    Returns:
        None
    """
    levels_in_m = [i * (station.typical_range[1] - station.typical_range[0]) + station.typical_range[0] 
                    for i in levels]
    plt.plot(dates, levels_in_m)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

