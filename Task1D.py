from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """
    Task 1D Demonstration: Tian Ern (Completed)
    """

    ############### DEMONSTRATION 1 ###############
    print("***DEMONSTRATION 1: geo.rivers_with_station***")

    # Build a set of river names
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)

    # Convert to list and sort
    rivers_list = list(rivers_set)
    rivers_list.sort()
    
    # Print output
    print("{} stations: First 10 - {}".format(len(rivers_list), rivers_list[:10]))
    print("\n")
    
    ############### DEMONSTRATION 2 ###############
    print("***DEMONSTRATION 2: geo.stations_by_river***")
    rivers_to_stations_dict = stations_by_river(stations)
    
    # River Aire
    stations_list = []
    for station in rivers_to_stations_dict["River Aire"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("Stations located on River Aire: {}\n".format(stations_list))

    # River Cam
    stations_list = []
    for station in rivers_to_stations_dict["River Cam"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("Stations located on River Cam: {}\n".format(stations_list))

    # River Thames
    stations_list = []
    for station in rivers_to_stations_dict["River Thames"]:
        stations_list.append(station.name)
    stations_list.sort()
    print("Stations located on River Thames: {}\n".format(stations_list))


if __name__ == "__main__":
    print("*** Task 1D: Tian Ern***")
    run()