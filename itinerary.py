"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Itinerary.

@file itinerary.py
"""
import math
from city import City, create_example_cities, get_cities_by_name

class Itinerary():
    """
    A sequence of cities.
    """

    def __init__(self, cities: list[City]) -> None:
        """
        Creates an itinerary with the provided sequence of cities,
        conserving order.
        :param cities: a sequence of cities, possibly empty.
        :return: None
        """
        #TODO
        # inputs attribute cities in a list of cities
        self.cities = list(cities)


    def total_distance(self) -> int:
        """
        Returns the total distance (in km) of the itinerary, which is
        the sum of the distances between successive cities.
        :return: the total distance.
        """
        #TODO
        # dist is set to 0  
        dist = 0 
        
        # sets the previous city to None
        previous = None
        
        # loops through the range of cities list
        for city in self.cities:

            # checks if it is at the end of the list
            if previous !=None:
                
                # adds the distance from one city to another, right until the end
                dist += previous.distance(city)

            # sets current city to previous city , then loops through again    
            previous = city
        
        # returns the total distance travelled from one point until the very end of the itinerary 
        return dist

    def append_city(self, city: City) -> None:
        """
        Adds a city at the end of the sequence of cities to visit.
        :param city: the city to append
        :return: None.
        """
        #TODO

        # appends the city to the list
        self.cities.append(city)

    def min_distance_insert_city(self, city: City) -> None:
        """
        Inserts a city in the itinerary so that the resulting
        total distance of the itinerary is minimised.
        :param city: the city to insert
        :return: None.
        """
        #TODO
        
        # loops through the cities list
        for i in range(len(self.cities)-1):

            #calculates the distances between city insert and city interary
            city_itin= self.cities[i].distance(self.cities[i+1])
            city_insert = city.distance(self.cities[i+1])

            # if city ininerary is less in distance than city insert then insert
            if city_itin < city_insert:

                # if cities previous is the same don't add it and continue
                if self.cities[i-1] == city:
                    continue
                else:
                    # else insert
                    self.cities.insert(i,city)
            
    def __str__(self) -> str:
        """
        Returns the sequence of cities and the distance in parentheses
        For example, "Melbourne -> Kuala Lumpur (6368 km)"

        :return: a string representing the itinerary.
        """
        #TODO
        # create an variable with an empty string 
        result = ""

        # checks if list len is zero (meaning there are no cities within the list)
        if len(self.cities) != 0:

            # loops through the city list
            for i in range(len(self.cities)-1):

                # returns the start of the itinery map 
                result += f"{self.cities[i].name}" 
                result += " -> " 

            # adds the string output of the total distance covered and returns the final city
            result += f"{self.cities[len(self.cities)-1].name} "
            result += f"({self.total_distance()} km)"
    
        else:
            # there is nothing in the list retuns 0 km
            result += f"({0} km)"
        
        # return result
        return result


if __name__ == "__main__":

    test = Itinerary([])
    print(test)
    
    create_example_cities()
    test_itin = Itinerary([get_cities_by_name("Melbourne")[0],get_cities_by_name("Kuala Lumpur")[0]])
    print(test_itin)

    #we try adding a city
    test_itin.append_city(get_cities_by_name("Baoding")[0])
    print(test_itin)

    #we try inserting a city
    test_itin.min_distance_insert_city(get_cities_by_name("Sydney")[0])
    print(test_itin)

    #we try inserting another city
    test_itin.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test_itin)
    
    
    city1 = City('Melbourne', (-37.8136, 144.9631), 'primary', 1000000, 1)
    city2 = City('Sydney', (-33.8688, 151.2093), 'primary', 5000000, 2)
    city3 = City('Brisbane', (-27.4698, 153.0251), 'primary', 2000000, 3)
    itinerary = Itinerary([city1, city2, city3])
    city4 = City('Canberra', (-35.2809, 149.1300), 'primary', 2000000, 4)
    test = Itinerary([city1,city2,city3])
    test.min_distance_insert_city(get_cities_by_name("Canberra")[0])
    print(test)    
    