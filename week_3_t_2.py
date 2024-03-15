'''. Write a program that takes N number of integers as
input and puts them in a list. Then it should find out
the maximum and minimum number from the list
and print them out. The whole list must also be
printed out.
'''
#Creating empty list
array = []

#taking data from user
a = int(input("Enter the number of elemts u want to keep in list"))

#for loop for adding element to the list given by user
for i in range (a):
    c = int(input("Enter the element of list"))
    array.append(c)

# Initialize max and min with the first element
max_number = array[0]
min_number = array[0]

# Iterate through the list to find actual max and min
for number in array:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

# Print the original list
print("Original list:", array)

# Print the maximum and minimum numbers
print("Maximum number:", max_number)
print("Minimum number:", min_number)
