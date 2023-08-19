"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It puts together all parts of the assignment.

@file onboard_navigation.py
"""

# all imports are required for function to be operating
from city import City
from country import Country
from itinerary import Itinerary
from vehicles import Vehicle , create_example_vehicles
from map_plotting import plot_itinerary
from csv_parsing import create_cities_countries_from_csv
from path_finding import find_shortest_path

# plugs all the results into the function plot itinerary and find_shortest_path functions
def On_board_nav(vehicle: Vehicle , from_city: City, to_city: City) -> Itinerary | map:
    
    # adds all cities into an itinerary
    # computes the shortest path
    if find_shortest_path(vehicle, from_city , to_city) is not None: 

        #if the shortest path exists, it plots the itinerary on a map
        print(find_shortest_path(vehicle, from_city , to_city))
        plot_itinerary(find_shortest_path(vehicle, from_city , to_city))

    
if __name__ == "__main__":
    # creates a variable using the list in the test cases
    vehicles = create_example_vehicles()
    
    # insert a random integer to store a list as [0,CCC,DDD,TTT]
    #vehicles.insert(0,0)
    
    # gets all the data from the csv file and stores all of them in city and class variables. 
    create_cities_countries_from_csv("worldcities_truncated.csv")
    
    # find the variable for the origin input string 
    def validate_itin1() -> City:
        while True:
            try:
                # tries to see if the user input works 
                user_city1 = str(input("What is the first would you like to travel to? "))
                City.name_to_cities[user_city1]
            except KeyError:
                print("Invalid input, please try again.")
            else:

                # returns the city object
                return City.name_to_cities[user_city1][0]
    
    # stores user input as a variable
    origin_city = validate_itin1()

    # find the variable for the final destination input string 
    def validate_itin2() -> City:
        while True:
            try:
                user_city2 = input("What is the second would you like to travel to? ")
                City.name_to_cities[user_city2]
            except KeyError:
                print("Invalid input, please try again.")
            else:

                # returns the city object
                return City.name_to_cities[user_city2][0]
            
    # stores user input as a variable
    final_dest_city = validate_itin2()


    # uses an infinite while loop to get the user to select 0 , 1 or 2 to get a vehicle type
    def validate_vehicle() -> Vehicle:
        while True: # sets up an inifinite loop until the return function is initiated / while false would terminate the code completely.
            try:
                user_vehicle = int(input("what vehicle would you like to use? (select 1 for CrappyCrepeCar , 2 for DiplomacyDonutDinghy or 3 for TeleportingTarteTrolley) "))
            except ValueError:
                print("Invalid input, please try again.")
            else:
                # if user input is in the range of values in list
                if user_vehicle in [1,2,3]:

                    # retuns the vehicle type
                    return vehicles[user_vehicle-1]


    # stores user input as a variable
    vehicle_choice = validate_vehicle()

    
    # items are inputed into the final function which returns the result
    On_board_nav(vehicle_choice, origin_city, final_dest_city)
    