import json
import re
import csv

# Write a function which count number of lines and number of words 
# in a text. All the files are in the data the folder: a) Read
# obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of
# lines and words c) Read donald_speech.txt file and count number
# of lines and words d) Read melina_trump_speech.txt file and count
# number of lines and words
def num_of_lines_and_words(name_file):
    num_of_lines = 0
    num_words = 0

    with open(name_file, "r") as file:
        for line in file:
            num_of_lines += 1
            words = line.split()
            num_words += len(words)
        
    return num_of_lines, num_words

obama_lines, obama_words = num_of_lines_and_words("./day_19/obama_speech.txt")
print("Obama Speech. Lines : %d\t Words: %d" %(obama_lines, obama_words))
michelle_lines, michelle_words = num_of_lines_and_words("./day_19/michelle_obama_speech.txt")
print("Michelle Speech. Lines : %d\t Words: %d" %(michelle_lines, michelle_words))
trump_lines, trump_words = num_of_lines_and_words("./day_19/donald_speech.txt")
print("Trump Speech. Lines : %d\t Words: %d" %(trump_lines, trump_words))
melina_lines, melina_words = num_of_lines_and_words("./day_19/melina_trump_speech.txt") 
print("Melina Speech. Lines : %d\t Words: %d" %(melina_lines, melina_words))

# Read the countries_data.json data file in data directory, create a function
# that finds the ten most spoken languages
def most_spoken_languages_json(filename, max):
    languages = {}
    with open(filename, encoding = "utf-8") as file:
        countries = json.loads(file.read())
        for country in countries:
            for language in country.get("languages"):
                languages[language] = languages.get(language, 0) + 1
        most_10_languages = sorted(languages.items(), key = lambda x: x[1], reverse = True)[:max]
    return most_10_languages

print(most_spoken_languages_json("./day_19/countries_data.json", 3))

# Read the countries_data.json data file in data directory, create a function 
# that creates a list of the ten most populated countries
def most_populated_countries(filename, max):
    country_population = {}
    list_most = []
    with open(filename, encoding = "utf-8") as file:
        countries = json.loads(file.read())
        for country in countries:
            country_population[country["name"]] = country["population"]
        most_10_populated = sorted(country_population.items(), key = lambda x: x[1], reverse = True)[:max]
        for i in range(max):
            aux = most_10_populated[i]
            most_10_populated[i] = {}
            most_10_populated[i]["country"] = aux[0]
            most_10_populated[i]["population"] = aux[1]
    return most_10_populated

print(most_populated_countries("./day_19/countries_data.json", 3))

## LEVEL 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

def extract_email_addresses(filename):
    email_addresses = []
    with open(filename, 'r') as file:
        for line in file:
            # Utilizamos una expresión regular para buscar las direcciones de correo electrónico en cada línea
            match = re.search(r'^From:\s*(\S+)', line)
            if match:
                email_addresses.append(match.group(1))
    return email_addresses

filename = './day_19/email_exchanges_big.txt'
email_list = extract_email_addresses(filename)
print(email_list)

# Find the most common words in the English language. Call the name of your function 
# find_most_common_words, it will take two parameters - a string or a file and a positive 
# integer, indicating the number of words. Your function will return an array of tuples 
# in descending order. Check the output
def find_most_common_words(filename, max):
    words_unique = {}
    with open(filename) as file:
        text = file.read()
        words_text = text.lower().split()
        for word in words_text:
            words_unique[word] = words_unique.get(word, 0) + 1
        most_used_words = sorted(words_unique.items(), key = lambda x: x[1], reverse = True)[:max]
    return most_used_words

# Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
print(find_most_common_words("./day_19/obama_speech.txt", 10))
# b) The ten most frequent words used in Michelle's speech
print(find_most_common_words("./day_19/michelle_obama_speech.txt", 10))
# c) The ten most frequent words used in Trump's speech 
print(find_most_common_words("./day_19/donald_speech.txt", 10))
# d) The ten most frequent words used in Melina's speech
print(find_most_common_words("./day_19/melina_trump_speech.txt", 10))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_stop_words(text):
    words = text.split()
    stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):

    # Clean and remove stop words from the texts
    clean_text1 = remove_stop_words(clean_text(text1))
    clean_text2 = remove_stop_words(clean_text(text2))

    # Calculate the similarity score (Jaccard similarity)
    words1 = set(clean_text1.split())
    words2 = set(clean_text2.split())
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    similarity = len(intersection) / len(union)

    return similarity

with open('./day_19/michelle_obama_speech.txt', 'r') as file:
    michelle_speech = file.read()
    
with open('./day_19/melina_trump_speech.txt', 'r') as file:
    melina_speech = file.read()

similarity_score = check_text_similarity(michelle_speech, melina_speech)
print(f"Similarity score: {similarity_score:.2f}")

# Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_common_words("./day_19/romeo_and_juliet.txt", 10))

# Read the hacker news csv file and find out: 
# a) Count the number of lines containing python or Python 
# b) Count the number lines containing JavaScript, javascript or Javascript 
# c) Count the number lines containing Java and not JavaScript
with open("./day_19/hacker_news.csv") as file:
    csv_reader = csv.reader(file, delimiter = ",")
    lines_with_python = 0
    lines_with_javascript = 0
    lines_with_java = 0
    next(csv_reader)
    for row in csv_reader:
        if "python" in row[1].lower():
            lines_with_python += 1
        if "javascript" in row[1].lower():
            lines_with_javascript += 1
        if "java" in row[1].lower() and "javascript" not in row[1].lower():
            lines_with_java += 1

print(lines_with_python)
print(lines_with_javascript)
print(lines_with_java)