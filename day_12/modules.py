import random
import string

# Write a function which generates a six digit/character random_user_id
def random_user_id():
    characters = string.ascii_lowercase + string.digits
    id = ""
    for i in range(6):
        id += characters[random.randint(0,len(characters)-1)]
    return id

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is 
# the number of IDs which are supposed to be generated.

def random_user_ids(numChar, numIds):
    characters = string.ascii_lowercase + string.digits
    ids = ""
    for x in range(numIds):
        for i in range(numChar):
            ids += characters[random.randint(0,len(characters)-1)]
        ids += "\n"
    return ids

print(random_user_ids(int(input("Cuantas letras?: ")), int(input("Cuantos IDs?: "))))

# Write a function named rgb_color_gen. It will generate rgb colors 
# (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    string = "rgb("
    string += str(random.randint(0,255))
    for i in range(2):
        string += "," + str(random.randint(0, 255))
    string += ")"
    return string

print(rgb_color_gen())

## LEVEL 2
# Write a function list_of_hexa_colors which returns any number of 
# hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 
# letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(numList):
    characters = string.ascii_lowercase[:7] + string.digits
    listHexa = []
    for i in range(numList):
        hexaColor="#"
        for x in range(6):
            hexaColor += characters[random.randint(0, len(characters) - 1)]
        listHexa.append(hexaColor)
    return listHexa

print(list_of_hexa_colors(4))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(numList):
    listRgb = []
    for i in range(numList):
        string = "rgb("
        string += str(random.randint(0,255))
        for x in range(2):
            string += "," + str(random.randint(0, 255))
        string += ")"
        listRgb.append(string)
    return listRgb

print(list_of_rgb_colors(4))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(typeColor, numList):
    if typeColor == "hexa":
        characters = string.ascii_lowercase[:7] + string.digits
        listHexa = []
        for i in range(numList):
            hexaColor="#"
            for x in range(6):
                hexaColor += characters[random.randint(0, len(characters) - 1)]
            listHexa.append(hexaColor)
        print(listHexa)
    elif typeColor == "rgb":
        listRgb = []
        for i in range(numList):
            string2 = "rgb("
            string2 += str(random.randint(0,255))
            for x in range(2):
                string2 += "," + str(random.randint(0, 255))
            string2 += ")"
            listRgb.append(string2)
        print(listRgb)
    else:
        print("Error")

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

## LEVEL 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list (listParam):
    aux = []
    for x in range(len(listParam)):
        aux.insert(random.randint(0, len(aux)), listParam[x])
    return aux

print(shuffle_list(["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]))

# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
def seven_numbers():
    array = []
    while len(array) < 7:
        num = random.randint(0, 9)
        if num not in array:
            array.append(num)
    print(array)

seven_numbers()