import numpy as np
from datetime import datetime


def polyfit(dates, levels, p):
    """
    Task 1F by Tian Ern
    Args:
        dates: list of datetime object
        levels: list of levels
        p: degree of polynomial

    Returns:
        a tuple of (i) the polynomial object and (ii) any shift of the time (date) axis
    """
    # get a datetime that is equal to epoch
    reference_time = dates[0]
    date_in_float = [(d - reference_time).total_seconds() for d in dates]
    return np.polyfit(date_in_float, levels, p)
