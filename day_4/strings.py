space = " "
string1 = "Thirty" + space + "Days" + space + "of" + space + "Python"
company = "Coding" + space + "for" + space + "All" 

print(company)
print(len(company))
print (company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[len("Coding"):len(company)])
print(company.index("Coding") >= 0)
print(company.replace("Coding", "Python"))
print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(", "))

print(company[0])
print(company[len(company)-1])
print(company[10])

aux = "Python For Everyone".split()
print("%s%s%s" %(aux[0][0], aux[1][0], aux[2][0]))

aux2 = (company.title()).split()
print("%s%s%s" %(aux2[0][0], aux2[1][0], aux2[2][0]))

print(company.index("C"))
print(company.title().index("F"))
print((company + "People").rfind("l"))

print("You cannot end a sentece with because because because is a conjuction".index("because"))
print("You cannot end a sentece with because because because is a conjuction".rindex("because"))
aux = "You cannot end a sentece with because because because is a conjuction".split(" because because because")
print(aux[0] + aux[1])

print(company.startswith("Coding"))
print(company.endswith("coding"))
aux2 = "   " + company + "      "
print(aux2.strip())

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(python_libraries))

print("I an enjoying this challenge.\n" +
      "I just wonder what is next")

print("Name\t\tAge\tCountry\tCity\n" +
      "Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

print("8 + 6 = {}".format(8 + 6))
print("8 - 6 = {}".format(8 - 6))
print("8 * 6 = {}".format(8 * 6))
print("8 / 6 = {:.2f}".format((8 / 6)))
print("8 % 6 = {}".format(8 % 6))
print("8 // 6 = {}".format(8 // 6))
print("8 ** 6 = {}".format(8 ** 6))