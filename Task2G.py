"""
Task 2G by Rajiv
"""

import datetime
import numpy as np
from floodsystem.datafetcher import fetch, fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation, relt_level
from floodsystem.flood import stations_level_over_threshold


def run():
    """
    Warning system
    1) Obtain a list of stations where the current relative level is already high
        (Threshold set at 1)
    2) For these stations, query the past 2 days data and find their fitting curves respectively
    3) From the fitting curves, predict the water level in the next hour
    """
    stations = build_station_list()
    update_water_levels(stations)
    list_of_stations_levels = stations_level_over_threshold(stations, 1)  # Note list of tuples

    dt=2
    t=176400  # next hour from now - it is number of seconds from two days ago
    s_tol = 10
    h_tol = 3
    m_tol = 1
    risk = 0
    severe_warnings = [[],[],[]]
    for station, _ in list_of_stations_levels:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if dates != None and levels != None:
            coeffs = polyfit(dates, levels, 3)
            poly = np.poly1d(coeffs)
            rel_level = relt_level(poly(t), station)
            if rel_level != None:
                if rel_level > s_tol:
                    # risk = "Severe"
                    severe_warnings[0].append((station.name,rel_level))
                elif rel_level > h_tol:
                    # risk = "High"
                    severe_warnings[1].append((station.name,rel_level))
                elif rel_level > m_tol:
                    # risk = "Moderate"
                    severe_warnings[2].append((station.name,rel_level))
    print("WARNING: These stations have a SEVERE risk of flooding:\n"+str(severe_warnings[0]))
    print("\n\n")
    print("WARNING: These stations have a HIGH risk of flooding:\n"+str(severe_warnings[1]))
    print("\n\n")
    print("WARNING: These stations have a MODERATE risk of flooding:\n"+str(severe_warnings[2]))

if __name__ == "__main__":
    run()


        
    
    
    

    



