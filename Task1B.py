"""
Task 1B by Rajiv
"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    '''Task 1B demonstration program by Rajiv'''
    stations = build_station_list()
    all_stations = stations_by_distance(stations, (52.2053, 0.1218))
    closest_10 = []
    farthest_10 = []

    for station, distance in all_stations[:10]:
        closest_10.append((station.name, station.town, distance))

    for station, distance in all_stations[-10:]:
        farthest_10.append((station.name, station.town, distance))

    print("Closest 10 Stations: {}".format(closest_10))
    print("Farthest 10 Stations: {}".format(farthest_10))

if __name__ == "__main__":
    run()