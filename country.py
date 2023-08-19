"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains the class Country.

@file country.py
"""
from tabulate import tabulate
from city import City, create_example_cities

class Country():
    """
    Represents a country.
    """

    name_to_countries = dict() # a dict that associates country names to instances.

    def __init__(self, name: str, iso3: str) -> None:
        """
        Creates an instance with a country name and a country ISO code with 3 characters.

        :param country_name: The name of the country
        :param country_iso3: The unique 3-letter identifier of this country
	    :return: None
        """
        self.name = name
        self.iso3 = iso3
        #TODO
        
        # create an empty list using the country class variable
        self.cities = []

        # adds the country class to a dictionary using country name as key and instance variable as value
        Country.name_to_countries[self.name] = self

    def add_city(self, city: City) -> None:
        """
        Adds a city to the country.

        :param city: The city to add to this country
        :return: None
        """
        #TODO        
        # appends a different city to the end of list in the country class
        self.cities.append(city)

    def get_cities(self, city_type: list[str] = None) -> list[City]:
        """
        Returns a list of cities of this country.

        The argument city_type can be given to specify a subset of
        the city types that must be returned.
        Cities that do not correspond to these city types are not returned.
        If None is given, all cities are returned.

        :param city_type: None, or a list of strings, each of which describes the type of city.
        :return: a list of cities in this country that have the specified city types.
        """
        #TODO
        #making an empty list
        city_list = []

        # if check if the city type is none
        if city_type is None:

            # if it is it will return all cities 
            return self.cities
        
        # loop through all the cities
        for i in range(len(self.cities)):

            # checks if the city type is in city type list
            if self.cities[i].city_type in city_type:

                # if it is, it appends it to the list
                city_list.append(self.cities[i])

        # retuns the name of the city of the list
        return city_list
    

    def print_cities(self) -> None:
        """
        Prints a table of the cities in the country, from most populous at the top
        to least populous. Use the tabulate module to print the table, with row headers:
        "Order", "Name", "Coordinates", "City type", "Population", "City ID".
        Order should start at 0 for the most populous city, and increase by 1 for each city.
        """
        #TODO 

        # prints the title w/ city name 
        print(f"Cities of {self.name}")

        # sorts all cities by population being the key and set reverse to true so it shows the population from descending order
        self.cities = sorted(self.cities,key=lambda city: city.population,reverse=True)
        
        # creates an empty list
        table_data = []

        # uses enumerate function to store the city information into a list inside table data
        for i, city in enumerate(self.cities):
            table_data.append([i, city.name, city.coordinates, city.city_type, city.population, city.city_id])
        headers = ["Order", "Name", "Coordinates", "City type", "Population", "City ID"]
        table = [headers]

        # for loop through the table and each element within the list into table 
        for i in range(len(table_data)):
            table.append(table_data[i])

        # print tabulate talbe 
        print(tabulate(table))    
   

    def __str__(self) -> str:
        """
        Returns the name of the country.
        """
        #TODO
        # stores country name in a varialbe and stored as a string
        value = f"{self.name}"

        # returns the variable value 
        return value
                

def add_city_to_country(city: City, country_name: str, country_iso3: str) -> None:
    """
    Adds a City to a country.
    If the country does not exist, create it.

    :param country_name: The name of the country
    :param country_iso3: The unique 3-letter identifier of this country
    :return: None
    """
    #TODO
    #works 
    
    # check if the country already exists
    if country_name in Country.name_to_countries:

        # retrieve the existing Country instance
        cur_country = Country.name_to_countries[country_name]
        cur_country.cities.append(city)
        
    else:
        # create a new Country instance
        new_country = Country(country_name, country_iso3)

        #print(new_country.cities)
        new_country.cities.append(city) 


def find_country_of_city(city: City) -> Country:
    """
    Returns the Country this city belongs to.
    We assume there is exactly one country containing this city.

    :param city: The city.
    :return: The country where the city is.
    """
    #TODO
    # get all keys in the country class 
    keys = Country.name_to_countries.keys()
    
    # loop through each of the items within name to country dictionary
    for item in keys:
        Country.name_to_countries[item]

        # if the city is contained within the country class dictionary
        if city in Country.name_to_countries[item].cities:

            # return the country name
            return Country.name_to_countries[item]
  

def create_example_countries() -> None:
    """
    Creates a few countries for testing purposes.
    Adds some cities to it.
    """
    create_example_cities()
    malaysia = Country("Malaysia", "MAS")
    kuala_lumpur = City.name_to_cities["Kuala Lumpur"][0]
    malaysia.add_city(kuala_lumpur)

    for city_name in ["Melbourne", "Canberra", "Sydney"]:
        add_city_to_country(City.name_to_cities[city_name][0], "Australia", "AUS")

def test_example_countries() -> None:
    """
    Assuming the correct countries have been created, runs a small test.
    """
    Country.name_to_countries["Australia"].print_cities()


if __name__ == "__main__":
    create_example_countries()
    test_example_countries()
