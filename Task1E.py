from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """
    Task 1E Demonstration: Tian Ern (Completed)
    """
    stations = build_station_list()
    listoftuples = rivers_by_station_number(stations, 9)
    print(listoftuples)


if __name__ == "__main__":
    print("*** Task 1E: Tian Ern***")
    run()