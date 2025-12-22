#  Write a Python program to print the square of each number in a list using a loop

list = [1, 2, 3]
square_list =[]

for number in list:
    square = number**2
    square_list.append(square)

print (square_list)
