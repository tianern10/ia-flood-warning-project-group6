# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """
    Task 1B by Rajiv (Completed)

    Output: Sorted list of (station, distance)
    """
    stations_and_distance = []
    sorted_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        stations_and_distance.append((station, distance))
    sorted_list = sorted_by_key(stations_and_distance, 1)
    return sorted_list


def stations_within_radius(stations, centre, r):
    """
    Task 1C by Rajiv (Completed)

    Output: List of stations within radius r

    """
    stations_within_r = []
    stations_and_distances = stations_by_distance(stations, centre)
    for station, distance in stations_and_distances:
        if distance < r:
            stations_within_r.append(station)
    return stations_within_r

def rivers_with_station(stations):
    """
    Task 1D by Tian Ern (Completed)
    Return a set with the names of the rivers with a monitoring station
    """
    rivers_set = set()
    for station in stations:
        if station.river != None:
            rivers_set.add(station.river)
    
    return rivers_set


def stations_by_river(stations):
    """
    Task 1D by Tian Ern (Completed)
    Return a dictionary that maps river names to a list of station objects
    """
    rivers_to_stations_dict = dict()
    for station in stations:
        if station.river in rivers_to_stations_dict:
            rivers_to_stations_dict[station.river].append(station)
        else:
            rivers_to_stations_dict[station.river] = []
            rivers_to_stations_dict[station.river].append(station)
    return rivers_to_stations_dict


def rivers_by_station_number(stations, N):
    """
    Task 1E by Tian Ern (Completed)
    Return a list of (river name, number of stations) tuples
    """
    rivers_to_stations_dict = stations_by_river(stations)
    rivers_tuples = []

    for key, listofstations in rivers_to_stations_dict.items():
        rivers_tuples.append((key, len(listofstations)))
    rivers_tuples.sort(key=lambda t : t[1], reverse=True)

    # Check if there are more rivers with the same number of stations as the N th entry
    k = N-1
    while True:
        if rivers_tuples[k][1] == rivers_tuples[k+1][1]:
            k+=1
        else:
            break
    return rivers_tuples[:k+1]

