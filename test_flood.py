"""
Unit test for flood module
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

def test_stations_level_over_threshold():
    stations = build_station_list()
    over_threshold = stations_level_over_threshold(stations, 0.8)
    assert isinstance(over_threshold, list)
    assert len(over_threshold) < len(stations)

def test_stations_highest_rel_level():
    stations = build_station_list()
    N = 10
    highest_rel_level = stations_highest_rel_level(stations, N)
    assert isinstance(highest_rel_level, list)
    assert len(highest_rel_level) == N
    

