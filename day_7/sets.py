# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the legth of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Nvidia", "Meta"])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Meta")
print(it_companies)

# What is the difference between remove and discard
it_companies.discard("Corsair")

## LEVEL 2
# Join A and B
union = A.union(B)
print(union)

# Find A intersection B
intersection = A.intersection(B)
print(intersection)

# Is a subset of B
print("Is a subset of B?: ",A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets? ", A.isdisjoint(B))

# What is the symmetric difference between A and B
print("What is the symmetric difference between A and B? ", A.symmetric_difference(B))

# Delete the sets comopletely
del A
del B

## LEVEL 3
# Convert the ages toa a set and compare the lenght of the list and the set , which one is bigger?
print(len(age))
age_set = set(age)
print(len(age_set))

# Explain the difference between the following data types
print("Un string es una estructura de datos que almacena un conjunto de letras, que forman una palabra")
print("Una lista es una colección que esta ordenado y puede ser modificado. Permite elementos duplicados")
print("Una tupla es una colección que esta ordenado pero no se puede ni cambiar ni modificar")
print("Un set es uan colección el cual esta desordenado, no es indexado ni modificable. No permite elementos duplicados")

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = set("I am a teacher and I love to inspire an teach people".split())
print(sentence)
print(len(sentence))