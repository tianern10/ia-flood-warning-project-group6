"""
Task 2E by Tian Ern
"""
from datetime import datetime, timedelta

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_highest_rel_level = stations_highest_rel_level(stations, 5)
    
    for station in list_of_highest_rel_level:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=10))
        plot_water_levels(station, dates, levels)
    


if __name__ == "__main__":
    print("*** Task 2E by Tian Ern: CUED Part IA Flood Warning System ***")
    run()
