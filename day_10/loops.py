# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    pass
counter = 0
while counter <= 10:
    print(counter)
    counter += 1

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, -1, -1):
    print(number)
counter = 10
while counter >= 0:
    print(counter)
    counter -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle
string = ""
for i in range(7):
    string += "#"
    print(string)

# Use nested loops to create the following:

for y in range(8):
    string = ""
    for x in range(8):
        string += "# "
    print(string)