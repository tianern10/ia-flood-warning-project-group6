"""
Unit test for the geo module
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation

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
    Task 1D by Tian Ern
    Check the function returns a dict where str -> MonitoringStation objects
    Check the function does not return an empty dict
    """
    stations = build_station_list()
    rivers_to_stations_dict = stations_by_river(stations)

    assert len(rivers_to_stations_dict) > 0
    assert isinstance(rivers_to_stations_dict, dict)
    for key, value in rivers_to_stations_dict.items():
        assert isinstance(key, str)
        assert isinstance(value, MonitoringStation)



    