from countryinfo import countries

countryinfo = countries

#Get a list of capital cities from the countryinfo.py file
capitals = [d['capital']for d in countryinfo]

#Get a list of countries from the countryinfo.py file
countrynames = [z["name"] for z in countryinfo]

#Generate  a dictionary of values from the two lists generated above

country_capitals = {}

for i in range(0,len(countrynames)):
    country_capitals[countrynames[i]] = capitals[i]




