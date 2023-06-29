from functools import reduce
import countries_mod
import countries_data


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
for i in countries:
    print(i)

# Use for to print each name in the names list.
for i in names:
    print(i)

# Use for to print each number in the numbers list.
for i in numbers:
    print(i)

## LEVEL 2
# Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(lambda x: x.upper(), countries)))

# Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda x: x ** 2, numbers)))

# Use map to change each name to uppercase in the names list
print(list(map(lambda x: x.upper(), names)))

# Use filter to filter out countries containing 'land'.
print(list(filter(lambda x: True if 'land' not in x else False, countries)))

# Use filter to filter out countries having exactly six characters.
print(list(filter(lambda x: True if len(x) != 6 else False, countries)))

# Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda x: True if len(x) < 6 else False, countries)))

# Use filter to filter out countries starting with an 'E'
print(list(filter(lambda country: not country.startswith("E"), countries)))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print(reduce(lambda num1, num2: num1 + num2, filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers))))

# Declare a function called get_string_lists which takes a list as a parameter and then 
# returns a list containing only string items.
def get_string_list(lst):
    return list(filter(lambda x: type(x) == str, lst))

# Use reduce to sum all the numbers in the numbers list.
print(reduce(lambda num1, sum2: num1 + sum2, numbers))

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, 
# Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print(reduce(lambda str, str2: str + ", " + str2, countries)[: -(len(countries[-1]) + 2)] + " and " + countries[-1] + " are north European countries")

# Declare a function called categorize_countries that returns a list of countries with 
# some common pattern (you can find the countries list in this repository as 
# countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern, lst):
    return list(filter(lambda country: pattern in country or pattern.capitalize() in country, lst))

print(categorize_countries("land", countries_mod.countries))
print(categorize_countries("ia", countries_mod.countries))
print(categorize_countries("island", countries_mod.countries))
print(categorize_countries("stan", countries_mod.countries))

# Create a function returning a dictionary, where keys stand for starting letters of 
# countries and values are the number of country names starting with that letter.
def dict_starting_letters(lst):
    dct = dict()
    for item in lst:
        dct[item[0]] = dct.get(item[0], 0) + 1
    return dct

print(dict_starting_letters(countries_mod.countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries 
# from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries_mod.countries[:10]

print(get_first_ten_countries())

# Declare a get_last_ten_countries function that returns the last ten countries in the 
# countries list.
def get_last_ten_countries():
    return countries_mod.countries[-10:]

print(get_last_ten_countries())

# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 
# file and follow the tasks below:

# Sort countries by name, by capital, by population
countries_sorted_name = sorted(countries_data.ns, key = lambda x: x["name"])
print("Ordenado por nombre:")
for country in countries_sorted_name:
    print(country["name"])

countries_sorted_capital = sorted(countries_data.ns, key = lambda x: x["capital"])
print("Ordenado por capital:")
for country in countries_sorted_capital:
    print(country["name"])

countries_sorted_population = sorted(countries_data.ns, key = lambda x: x["population"], reverse = True)
print("Ordenado por population:")
for country in countries_sorted_population:
    print(country["name"])

# Sort out the ten most spoken languages by location.
def agrup_language(lst):
    dct = {}
    for country in lst:
        for language in country.get("languages"):
            dct[language] = dct.get(language, 0) + country.get("population")
    return dct


hola = agrup_language(countries_data.ns)
languages_sorted = sorted(hola, key = lambda x: hola[x], reverse = True)[:10]
print(languages_sorted)