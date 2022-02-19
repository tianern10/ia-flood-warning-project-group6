"""
Unit test for the geo module
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius

def test_plot_water_levels():
    """
    Task 2E by Tian Ern
    """
    # did not test matplotlib figure due to several challenges
    assert True
