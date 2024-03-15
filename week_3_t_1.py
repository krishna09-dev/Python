''' Write a program that takes N numbers as input from a user and puts them in a list.
Then the program should find out the sum of all the odd numbers and
the sum of all the even numbers from the list. '''

array = []
a = int(input("Enter the number of elemts u want to keep in list"))
for i in range (a):
    c = int(input("Enter the element of list"))
    array.append(c)

even_sum = 0
odd_sum = 0
for num in array:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

    
