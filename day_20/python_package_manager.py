import requests
import json
import sys

# Read this url and find the 10 most frequent words. romeo_and_juliet
#  = 'http://www.gutenberg.org/files/1112/1112.txt'

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

txt = requests.get(romeo_and_juliet).text.lower().split()
words_counter = {}
for word in txt:
    words_counter[word] = words_counter.get(word, 0) + 1

sorted_words = sorted(words_counter.items(), key = lambda x: x[1], reverse = True)[:10]
print(sorted_words)

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cats_api = 'https://api.thecatapi.com/v1/breeds'
cats_json = requests.get(cats_api).json()
# a) the min, max, mean, median, standard deviation of cats' weight in metric units.
arr_weight = []
for cat  in cats_json:
    range_weight = cat["weight"]["metric"].split(" - ")
    range_weight = [int(i) for i in range_weight]
    arr_weight += range_weight
arr_weight.sort()
min_weight = min(arr_weight)
max_weight = max(arr_weight)
mean_weight = sum(arr_weight) / len(arr_weight)
if len(arr_weight) % 2 == 0:
    median_weight = (arr_weight[int(len(arr_weight) / 2) - 1] + arr_weight[int(len(arr_weight) / 2)]) / 2
else:
    median_weight = arr_weight[int(len(arr_weight) / 2)]
deviation = [(x - mean_weight) ** 2 for x in arr_weight]
standard_deviation = (sum(deviation) / len(arr_weight)) ** 0.5

print(min_weight)
print(max_weight)
print(mean_weight)
print(median_weight)
print(standard_deviation)
# b) the min, max, mean, median, standard deviation of cats' lifespan in years.
arr_life_span = []
for cat  in cats_json:
    range_life_span = cat["life_span"].split(" - ")
    range_life_span = [int(i) for i in range_life_span]
    arr_life_span += range_life_span
arr_life_span.sort()
min_life_span = min(arr_life_span)
max_life_span = max(arr_life_span)
mean_life_span = sum(arr_life_span) / len(arr_life_span)
if len(arr_life_span) % 2 == 0:
    median_life_span = (arr_life_span[int(len(arr_life_span) / 2) - 1] + arr_life_span[int(len(arr_life_span) / 2)]) / 2
else:
    median_life_span = arr_life_span[int(len(arr_life_span) / 2)]
deviation = [(x - mean_life_span) ** 2 for x in arr_life_span]
standard_deviation = (sum(deviation) / len(arr_life_span)) ** 0.5

print(min_life_span)
print(max_life_span)
print(mean_life_span)
print(median_life_span)
print(standard_deviation)
# c) Create a frequency table of country and breed of cats
frequency_country = {}
for cat  in cats_json:
    frequency_country[cat["origin"]] = frequency_country.get(cat["origin"], 0) + 1

sorted_frequency = sorted(frequency_country.items(), key = lambda x: x[1], reverse = True)

print("País\t\t\tRazas")
for country in sorted_frequency:
    print("%s\t\t%d" %(country[0], country[1]))

# Read the countries API and find
countries_api = 'https://restcountries.eu/rest/v2/all'
countries_json = requests.get(countries_api).json()
# a) the 10 largest countries
for country in countries_json:
    print(country)