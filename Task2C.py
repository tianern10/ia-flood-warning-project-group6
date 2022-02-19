"""
Task 2C TODO
"""
from datetime import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_highest_stations = stations_highest_rel_level(stations, 10)

    for i in list_of_highest_stations:
        print(i.name, i.relative_water_level())
    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
