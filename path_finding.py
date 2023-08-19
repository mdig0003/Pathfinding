"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a function to create a path, encoded as an Itinerary, that is shortest for some Vehicle.

@file path_finding.py
"""
import math
import networkx as nx

from city import City, get_city_by_id
from itinerary import Itinerary
from vehicles import Vehicle, create_example_vehicles
from csv_parsing import create_cities_countries_from_csv
from itertools import combinations

def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Itinerary | None:
    """
    Returns a shortest path between two cities for a given vehicle as an Itinerary,
    or None if there is no path.

    :param vehicle: The vehicle to use.
    :param from_city: The departure city.
    :param to_city: The arrival city.
    :return: A shortest path from departure to arrival, or None if there is none.
    """
    
    #TODO
    G = nx.Graph()
    # puts all the objects into a list using a key
    data = []
    for key in City.name_to_cities:
        for city in City.name_to_cities[key]:
            data.append(city)
    
    # stores all values of n object into a list which contains two different cities connecting at different nodes
    diff_combination_list = list(combinations(data,2))

    # adding edges to all different nodes based on weight of time
    for city in diff_combination_list:
        time = vehicle.compute_travel_time(city[0] , city[1])

        # time is infinite continue
        if time == math.inf:
            continue
        else:
            # add an edge between the two cities in the tuple.
            G.add_edge(city[0],city[1])


    # try if the shortest path in networkx module. 
    try:
        path = nx.shortest_path(G,from_city,to_city)
    except:
        # if there is no shortest path for that vehicle then return none
        return None

    # add city to the itinerary 
    itinerary = []
    for item in path:
        itinerary.append(item)

    # returns the itinerary time
    return Itinerary(itinerary)
    

if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")
    vehicles = create_example_vehicles()

    from_cities = set()
    for city_id in [1036533631, 1036142029, 1458988644]:
        from_cities.add(get_city_by_id(city_id))

    #we create some vehicles
    vehicles = create_example_vehicles()

    to_cities = set(from_cities)
    for from_city in from_cities:
        to_cities -= {from_city}
        for to_city in to_cities:
            print(f"{from_city} to {to_city}:")
            for test_vehicle in vehicles:
                shortest_path = find_shortest_path(test_vehicle, from_city, to_city)
                print(f"\t{test_vehicle.compute_itinerary_time(shortest_path)}"
                      f" hours with {test_vehicle} with path {shortest_path}.")
