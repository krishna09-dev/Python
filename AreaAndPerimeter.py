'''Write a program that asks the user to input length and breadth of a rectangle.
Then the program should calculate to area and perimeter of the rectangle and
print them out. Area = l × b; Perimeter = 2(l + b);'''

# Enter the length of the rectangle
length = int(input("Enter the length of the rectangle: "))

# Enter the breadth of the rectangle
breadth = int(input("Enter the breadth of the rectangle: "))

# Calculate the area of the rectangle
area = length * breadth

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + breadth)

# Print the calculated area and perimeter
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
