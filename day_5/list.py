# Declare an empty list
list = list()

# Declare a list with more than 5 items
list = ["manzana", "limon", "pera", "coco", "naranja"]

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
print(list[0])
print(list[(len(list)//2)])
print(list[len(list)-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Albert", 20, 72, "Pareja", "Calle Ricard Ankerman"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(mixed_data_types)
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies)//2])
print(it_companies[len(it_companies)-1])

# Print the list after modifying one of the companies
it_companies[4] = "Nvidia"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Twitter")
print(it_companies)

# Change one of the it_companies name to uppercase
it_companies[it_companies.index("Nvidia")] = it_companies[it_companies.index("Nvidia")].upper()
print(it_companies)

# Join the it_companies with a string '#; '
#it_companies += "#; "
print(it_companies)

# Check if a certain company exists in the it_companies list.
print("NVIDIA" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
it_companiesFirst4 = it_companies[3:]
print(it_companiesFirst4)

# Slice out the last 3 companies from the list
it_companiesLast4 = it_companies[:len(it_companies)-3]
print(it_companiesLast4)

# Slice out the middle IT company or companies from the list
it_MiddleCompanies = it_companies[:(len(it_companies)//2)-1] + it_companies[(len(it_companies)//2)+1:]
print(it_MiddleCompanies)

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[3]
print(it_companies)

# Remove the last IT company from the list
del it_companies[len(it_companies)-1]
print(it_companies)

# remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following list
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
end = front_end + back_end
print(end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = end.copy()
full_stack.append("Python")
full_stack.append("SQL")
print (full_stack)

## LEVEL 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[len(ages)-1]

# Find the median age (one middle item or two middle items divided by two)
median_age = [ages[len(ages)//2]-1, ages[(len(ages)//2)]]
print(median_age)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages)/len(ages)

# Find the range of the ages (max minus min)
range = ages[len(ages)-1]- ages[0]
print("Range: ", range)

# Compare the value of (min - average) and (max - average), use abs() method
ns = abs(min_age - average_age)
ns2 = max_age - average_age
print("ns:", ns)
print("ns2:", ns2)

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

if len(countries) % 2 == 0:
    print(countries[len(countries)//2-1:len(countries)//2+1])
else:
    print(countries[len(countries)//2])

china, russia, usa, *scandic = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]

print(scandic)

print(ages)