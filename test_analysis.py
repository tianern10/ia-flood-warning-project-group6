"""
Unit test for the analysis submodule
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