import countryinfo
import shutil

country_capitals2 = {}
continents = ["Europe", "Asia", "Africa", "Oceania", "North America", "South America"]


def continentselector():
    global continents
    """a function to generate a dictionary with the countries name and capital city
     filtered out by the continent specified by the user"""
    while True:
        for num, cont in enumerate(continents):
            print(str(num) + " : " + cont)
        user_continent = int(input("\n Enter the digit corresponding to the continent: \n".strip()))
        user_continent = continents[user_continent]
        if user_continent:
            break
        else:
            continue
    # extract a list with countries information from the continent provided by the user
    continents = []
    for items in countryinfo.countries:
        if items["continent"].lower() == user_continent.lower():
            continents.append(items)
    # creating a list with the countries name
    countries_continents = [d["name"] for d in continents]
    # creating a list with the coutries capitals
    ccapitals_continents = [f["capital"] for f in continents]
    # group the two lists above to create a dictionary with information on countries name and capital
    for i in range(0, len(countries_continents)):
        country_capitals2[countries_continents[i]] = ccapitals_continents[i]


def delete_previous(location):
    """A simple function to deleted any provided folder location"""
    shutil.rmtree(location, ignore_errors=True, onerror=None)
