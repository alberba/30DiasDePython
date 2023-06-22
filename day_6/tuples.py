# Create an empty tuple
tuple = ()

# Create a tuple containing names of your sisters and your brothers
brothers = ("Jaume", "Juan", "Guille")
sisters = ("Aina", "Paula", "Paqui")

# Join brothers and sisters tuples and assign it to siblings
hermanos = brothers + sisters

# How many siblings you have?
print(len(hermanos))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = hermanos + ("Luis", "Joana")
print(family_members)

## LEVEL 2
# Unpack siblings and parents from family_members
siblings = family_members[:family_members.index("Luis")]
parents = family_members[family_members.index("Luis"):]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("manzana", "pera", "platano")
vegetables = ("tomate", "patata")
animal_products = ("pienso", "cepillo")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item o items from the food_stuff_lt list
food_stuff_lt2 = food_stuff_lt[:len(food_stuff_lt)//2]+food_stuff_lt[len(food_stuff_lt)//2+1:]
print(food_stuff_lt2)

# Sile out the first three items and the last three items from food_staff_lt
food_stuff_lt3 = food_stuff_lt[3:-3]
print(food_stuff_lt3)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)