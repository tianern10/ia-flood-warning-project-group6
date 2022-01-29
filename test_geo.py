"""
Unit test for the geo module
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius

def test_stations_by_distance():
    """
    Task 1B by Rajiv
    """
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053, 0.1218))
    assert isinstance(x, list)
    for i in x:
        assert isinstance(i, tuple)
        assert len(i) == 2
        assert isinstance(i[0], MonitoringStation)
        assert isinstance(i[1], float)

def test_stations_within_radius():
    """
    Task 1C by Rajiv (Incomplete)

    """
    stations = build_station_list()
    y = stations_within_radius(stations,(52.2053, 0.1218),20)
    assert isinstance(y, list)
    for i in y:
        assert isinstance(i, MonitoringStation)
        



def test_rivers_with_station():
    """
    Task 1D by Tian Ern (Completed)
    Check the function returns a set of string
    Check the function does not return an empty set
    """
    stations = build_station_list()
    rivers_set = rivers_with_station(stations)

    assert len(rivers_set) > 0
    assert isinstance(rivers_set, set)
    for river_name in rivers_set:
        assert isinstance(river_name, str)


def test_stations_by_river():
    """
    Task 1D by Tian Ern (Completed)
    Check the function returns a dict where str maps to list of MonitoringStation objects
    Check the function does not return an empty dict
    """
    stations = build_station_list()
    rivers_to_stations_dict = stations_by_river(stations)

    assert len(rivers_to_stations_dict) > 0
    assert isinstance(rivers_to_stations_dict, dict)
    for key, value in rivers_to_stations_dict.items():
        assert isinstance(key, str)
        assert isinstance(value, list)
        for i in value:
            assert isinstance(i, MonitoringStation)


def test_rivers_by_station_number():
    """
    Task 1E by Tian Ern (Completed)
    Check the function returns a list of (str, int) tuples
    Check that >Nth entry has the same number of stations as the Nth entry
    """
    N = 50
    stations = build_station_list()
    list_of_tuples = rivers_by_station_number(stations, N)

    # Check the function returns a list of (str, int) tuples
    assert isinstance(list_of_tuples, list)
    for t in list_of_tuples:
        assert isinstance(t, tuple)
        assert len(t)==2
        assert isinstance(t[0], str)
        assert isinstance(t[1], int)
    
    # Check that >Nth entry has the same number of stations as the Nth entry
    if len(list_of_tuples) > N:
        for i in range(N, len(list_of_tuples)):
            assert list_of_tuples[N-1][1] == list_of_tuples[i][1]