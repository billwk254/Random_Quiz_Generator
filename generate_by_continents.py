import countryinfo

country_capitals2 = {}

# a function to generate a dictionary with the countries name and capital city filtered out by the continent specified by the user
def continentselector():
    while True:
        user_continent = input("Please enter a continent to get the countries: \n".strip())
        if user_continent:
            break
        else:
            continue
#extract a list with countries information from the continent provided by the user
    continents = []
    for items in countryinfo.countries:
        if items["continent"].lower() == user_continent.lower():
            continents.append(items)
#creating a list with the countries name
    countries_continents = [d["name"] for d in continents]
#creating a list with the coutries capitals
    ccapitals_continents = [f["capital"] for f in continents]
#group the two lists above to create a dictionary with information on countries name and capital
    for i in range(0, len(countries_continents)):
        country_capitals2[countries_continents[i]] = ccapitals_continents[i]
