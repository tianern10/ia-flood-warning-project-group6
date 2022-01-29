"""
Task 1C by Rajiv
"""


from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

stations = build_station_list()
stations_in_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)

list_of_names = []

for i in stations_in_radius:
    list_of_names.append(i.name)

list_of_names.sort()

print(list_of_names)
