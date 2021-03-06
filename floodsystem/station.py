# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


from xml.sax.handler import DTDHandler


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   latest level:  {}".format(self.latest_level)
        return d
    
    def typical_range_consistent(self):
        """
        Task 1F: Tian Ern (Completed)
        Check the typical high/low range data for consistency and availability
        """
        if self.typical_range == None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True
    
    def relative_water_level(self):
        """
        Task 2B TODO
        """
        if self.typical_range_consistent() == True and self.latest_level != None:
            rel = (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
            # discard insensible value
            if rel > 100:
                return None
            else:
                return rel
        else:
            return None


def inconsistent_typical_range_stations(stations):
    """
    Task 1F: Tian Ern (Completed)
    Return a list of stations that have inconsistent data
    """
    list_of_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            list_of_stations.append(station)
    return list_of_stations

def relt_level(level, station):
    """
    Task 2G: Rajiv
    Input level, station
    Slightly changed relative_water_level so that any water level can be input (e.g. from predictions)
    Output: relative water level 
    """
    if station.typical_range_consistent() == True:
        rel = (level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])
        # discard insensible value
        if rel > 100:
            return None
        else:
            return rel
    else:
        return None

