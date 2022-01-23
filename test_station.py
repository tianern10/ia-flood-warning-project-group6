# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    """
    Test for Task 1F: Tian Ern
    Test for typical_range_consistent
    """
    # Create a station
    trange = (-2.3, 3.4445)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s2.typical_range_consistent() == True

    trange = (3.5, 3.4445)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s3.typical_range_consistent() == False

    trange = None
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s4.typical_range_consistent() == False

