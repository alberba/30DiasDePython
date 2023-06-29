# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

print([num for sublist in list_of_lists for subsublist in sublist for num in subsublist])

# Using list comprehension create the following list of tuples:
nose = [(i, *(i ** y for y in range(6))) for i in range(11)]
print(nose)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
cosas = [[country.upper(), country[:3].upper(), city.upper()] for [[country, city]] in countries]
print(cosas)

# Change the following list to a list of dictionaries:
list_dict = [{"country": country.upper(), "city": capital.upper()} for [[country, capital]] in countries]
print(list_dict)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
totalName = [name + " " + surname for [[name, surname]] in names]
print(totalName)

# Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1, y1, x2, y2, solve: (y2 - y1) / (x2 - x1) if solve == "slope" else y1 - ((y2 - y1)/ (x2 - x1)) * x1