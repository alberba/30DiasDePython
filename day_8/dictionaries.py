# Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = {"name":"Fosca", "color":"black", 
       "breed":"Border Collie", "legs":"grandes", 
       "age":"12"}

# Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary
student = {"first_name":"Albert", "last_name":"Salom", "gender":"masculino", 
           "age":19, "marital status":"pareja", "skills":["Informatica", "ser frances"],
           "country":"España","city":"Palma", "address":"Ricard Ankerman"}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and chek the data type, it should be al list
print(student["skills"])
print(type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("ser guapo")
student["skills"].append("ser alto")

# Get the dictionary keys as a list
keysList = list(student.keys())
print(keysList)

# Get the dictionary values as a list
valueList = list(student.values())
print(valueList)

# Change the dictionary to a list of tuples using items() method
listTuples = list(student.items())
print(type(listTuples))
print(type(listTuples[0]))

# Delete one of the items in the dictionary
student.popitem()

# Delete one of the dictionaries
del student