"""
This file is part of Assignment 2 of FIT1045, S1 2023.

It contains a parser that reads a CSV file and creates instances 
of the class City and the class Country.

@file city_country_csv_reader.py
"""
import csv
from city import City
from country import Country , add_city_to_country

def create_cities_countries_from_csv(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.

    :param path_to_csv: The path to the CSV file.
    """
    #TODO
    # reads csv files 
    with open(path_to_csv,'r', newline='', encoding='utf-8') as csvfile:

        # stores dictionary in rows 
        data = csv.DictReader(csvfile, delimiter=',')

        # loops through each elemenet in the dictionary 
        for row in data:

            # checks if population is an empty string
            if row['population'] == '':
                    
                    # if it is, it is set to zero
                    row['population'] = 0

            # stroes each dictionary value in the city class 
            city = City(str(row['city_ascii']), (float(row['lat']) , float(row['lng'])) , row['capital'] , int(row['population'] ), int(row['id']))

            # adds the city to country, so that results can be tabulated
            add_city_to_country(city , row['country'] , row['iso3'])
            


if __name__ == "__main__":
    create_cities_countries_from_csv("worldcities_truncated.csv")

    for country in Country.name_to_countries.values():
       country.print_cities()
