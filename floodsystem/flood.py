from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """
    Task 2B TODO
    Args:
        stations: list of MonitoringStation objects
        tol: threshold
    Returns:
        Decending List of (MonitoringStation, relative level) tuples
    """
    list_of_tuples = []
    for station in stations:
        if station.latest_level != None and station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                list_of_tuples.append((station, station.relative_water_level()))
    sorted_list_of_tuples = sorted_by_key(list_of_tuples, 1, True)
    
    return sorted_list_of_tuples


def stations_highest_rel_level(stations, N):
    """
    Task 2C TODO
    Most at risk stations
    Args:
        stations: list of MonitoringStations objects
        N: number of stations in output

    Returns:
        A list of MonitoringStation object
    """
    list_of_tuples = []
    for station in stations:
        if station.relative_water_level() != None:
            list_of_tuples.append((station, station.relative_water_level()))
    sorted_list_of_tuples = sorted_by_key(list_of_tuples, 1, True)
    output_list = [t[0] for t in sorted_list_of_tuples]
    
    return output_list[:N]