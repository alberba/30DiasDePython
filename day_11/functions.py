import countriesdata
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def calc_area_circle(r):
    pi = 3.14
    return (pi * (r ** 2))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) == int:
            sum += num
        else:
            print("Please enter only numbers.")
            return 0
    return sum

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which
# converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ("September", "October", "November"):
        return "Autumn"
    elif month in ("December", "January", "February"):
        return "Winter"
    elif month in ("June", "July", "August"):
        return "Summer"
    elif month in ("March", "April", "May"):
        return "Spring"
    else:
        print("Error")
        return 0
    
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which
# calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b , c):
    sol1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2*a)
    sol2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2*a)
    return sol1, sol2

# Declare a function named print_list. It takes a list as a parameter and it prints out
# each element of the list.
def print_list(list):
    for item in list:
        print(item)

# Declare a function named reverse_list. It takes an array as a parameter and it returns
# the reverse of the array (use loops).
def reverse_list(array):
    reversed_list = []
    for item in array:
        reversed_list.insert(0, item)
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it
# returns a capitalized list of items
def capitalize_list_items(list):
    capitalized_list = []
    for item in list:
        item = str(item)
        capitalized_list.append(item.capitalize())
    return capitalized_list

# Declare a function named add_item. It takes a list and an item parameters. It returns
# a list with the item added at the end.
def add_item(list, item):
    list.append(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

# Declare a function named remove_item. It takes a list and an item parameters. It returns
# a list with the item removed from it.
def remove_item(list, item):
    list.remove(item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the
# numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for x in range(num+1):
        sum += x
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd
# numbers in that range.
def sum_of_odds(num):
    sum = 0
    for x in range(num+1):
        if (x % 2) != 0:
            sum += x

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even
# numbers in that - range.
def sum_of_even(num):
    sum = 0
    for x in range(num+1):
        if (x % 2) == 0:
            sum += x

## LEVEL 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it
# counts number of evens and odds in the number.
def evens_and_odds(num):
    evens_count = 0
    odds_count = 0
    for x in range(101):
        if (x % 2) != 0:
            odds_count += 1
        else:
            evens_count += 1
    return "The number of odds are %d.\nThe number of evens are %d." %(odds_count, evens_count)


print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

# Call your function factorial, it takes a whole number as a parameter and it return a
# factorial of the number
def factorial(num):
    result = 1
    for x in range(1, num+1):
        result *= x
    return result

print(factorial(4))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(parameter):
    if not parameter:
        return True
    else:
        return False

## LEVEL 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if type(num) != int:
        return None
    if num < 2:
        return True
    for x in range(2, num/2+1):
        if num % x == 0:
            return False
    return True

# Write a functions which checks if all items are unique in the list.
def unique_item_list(list1):
    list1 = list(list1)
    for x in range(len(list1)-1):
        for y in range(x+1, len(list1)):
            if(list1[x] == list1[y]):
                return False
    return True

# Write a function which checks if all the items of the list are of the same data type.
def list_same_type(list1):
    typeList = type(list1[0])
    for x in range (1, len(list1)):
        if (typeList != list1[x]):
            return False
    return True

# Go to the data folder and access the countries-data.py file.
def most_spoken_languages(countries):
    language_dict = {}
    for country in countries:
        for language in country.get("languages"):
            language_dict[language] = language_dict.get(language,0) + 1

    top_10_languages = sorted(language_dict.items(), key = lambda x: x[1], reverse=True)[:10]
    return top_10_languages

# Create a function called the most_populated_countries. It should return 10 or 20 most
# populated countries in descending order.
def most_populated_countries (countries):
    top_10_populated = sorted(countries, key = lambda x: x["population"], reverse = True)[:10]
    return top_10_populated
