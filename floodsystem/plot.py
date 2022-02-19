import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from .datafetcher import fetch_measure_levels
from .analysis import polyfit


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
    # levels_in_m = [i * (station.typical_range[1] - station.typical_range[0]) + station.typical_range[0] 
    #                 for i in levels]
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')


    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """
    Task 2F by Tian Ern

    Args:
        station: a MonitoringStation object
        dates: list of datetime object
        levels: list of water levels in float

    Returns:
        None
    """
    p_coeff = polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)

    reference_time = dates[0]
    date_in_float = [(d - reference_time).total_seconds() for d in dates]
    date_in_float = np.array(date_in_float)

    plt.plot(dates, levels)
    plt.plot(dates, poly(date_in_float - date_in_float[0]))

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(y=station.typical_range[0], color='r', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')


    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
