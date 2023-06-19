# Day 2: 30 days of python programming

first_name = 'Albert'
last_name = 'Salom'
full_name = 'Albert Salom'
country = 'Spain'
city = 'Barcelona'
age = 30
year = 2021
is_married = False
is_true = True
is_light_on = False
name, surname, age, country = 'Albert', 'Salom', 30, 'Spain'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(surname))
print(type(age))
print(type(country))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

radius = int(input('Enter radius: '))
area_of_circle = 3.14 * (radius ** 2)
circum_of_cicle = 2 * 3.14 * radius

age = 30
height = 1.80
complex_num = 2j - 2

triangle_base = int(input('Enter base: '))
triangle_height = int(input('Enter height: '))
area_of_triangle = int((triangle_base * triangle_height) / 2)
print('The area of the triangle is', area_of_triangle)

sideATriangle = int(input('Enter side A: '))
sideBTriangle = int(input('Enter side B: '))
sideCTriangle = int(input('Enter side C: '))
perimeter_of_triangle = sideATriangle + sideBTriangle + sideCTriangle
print("The perimeter of the triangle is", perimeter_of_triangle)

length_rectangle = int(input("Enter length of the rectangle: "))
width_rectangle = int (input("Enter widht of the rectangle: "))
area_of_rectangle = length_rectangle * width_rectangle
perimeter_of_rectangle = 2 * (length_rectangle + width_rectangle)
print(area_of_rectangle)
print(perimeter_of_rectangle)

point1 = (2,2)
point2 = (6,10)

euclidean_distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
print("The Euclidan Distance is ", euclidean_distance)

print(len('python'))
print(len('dragon'))
print(len('python') == len('dragon'))
print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')
length_python = str(float(len('python')))

num = int(2.7)
num2 = 7 // 3
print(num == num2)

print(type('10') == type(10))
print(int(9.8) == 10)
hours = int(input('Enter hours: '))
rate = int(input('Enter rateper hour: '))
print("Your weekly earning is", (hours * rate))

years = int(input("Enter number of years you have lived: "))
print ("You have lived for", (years*365*24*3600), "seconds.")

print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
