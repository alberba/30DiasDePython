import countriesdata
# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    pass
counter = 0
while counter <= 10:
    print(counter)
    counter += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, -1, -1):
    print(number)
counter = 10
while counter >= 0:
    print(counter)
    counter -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle
string = ""
for i in range(7):
    string += "#"
    print(string)

# Use nested loops to create the following:

for y in range(8):
    string = ""
    for x in range(8):
        string += "# "
    print(string)

# Print the following pattern:
for x in range(11):
    string = "%d x %d = %d" %(x, x, (x ** 2))
    print(string)
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
for x in range (101):
    if (x % 2) == 0:
        print(x)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for x in range (101):
    if (x % 2) != 0:
        print(x)

## LEVEL 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for x in range(101):
    sum += x
print("The sum of all numbers is %d" %sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for x in range(101):
    if (x % 2) != 0:
        sum_odds += x
    else:
        sum_evens += x
print("The sum of all evens is %d. And the sum of all odds is %d." %(sum_evens, sum_odds))

## LEVEL 3
# Go to the data folder and use the countries.py file. Loop through the countries and
# extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for country in countries:
    if 'land' in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
language_list = set()
for country in countriesdata.countrydata:
    for language in country.get("languages"):
        language_list.add(language)
print(len(language_list))

language_dict = {}
for country in countriesdata.countrydata:
    for language in country.get("languages"):
        language_dict[language] = language_dict.get(language,0) + 1

top_10_languages = sorted(language_dict.items(), key = lambda x: x[1], reverse=True)[:10]
print(len(language_list))

# Find the 10 most populated countries in the world
top_10_populated = sorted(countriesdata.countrydata, key = lambda x: x["population"], reverse = True)[:10]
for country in top_10_populated:
    print("%s : %d" %(country["name"], country["population"]))