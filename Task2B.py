"""
Task 2B TODO
"""
from datetime import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_tuples = stations_level_over_threshold(stations, 0.8)
    for t in list_of_tuples:
        print(t[0].name, t[1])
    


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
