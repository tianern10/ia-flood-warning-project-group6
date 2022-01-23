from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """
    Task 1F Demonstration: Tian Ern
    Build a list of all stations with inconsistent typical range data
    """

    stations = build_station_list()
    list_of_stations = inconsistent_typical_range_stations(stations)
    list_of_station_names = [station.name for station in list_of_stations]
    list_of_station_names.sort()
    print(list_of_station_names)


if __name__ == "__main__":
    print("*** Task 1F: Tian Ern ***")
    print("The list of station names, in alphabetical order, for stations with inconsistent data")
    run()
