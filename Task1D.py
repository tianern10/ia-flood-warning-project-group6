from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """
    Requirements for Task 1A
    Written by Tian Ern
    """
    # Build a set of river names
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)

    # Convert to list and sort
    rivers_list = list(rivers_set)
    rivers_list.sort()
    
    # Print output
    print("{} stations: First 10 - {}".format(len(rivers_list), rivers_list[:10]))


if __name__ == "__main__":
    print("*** Task 1D: Tian Ern ***")
    run()