'''Write a program that computes the value of the algebraic expression:
x^3 + 3x^2y + 3xy^2 + y^3
The program should ask the user to input the values of x and y. Write
comments to describe your code. '''

# Enter the value of x
x = int(input("Enter the value of x: "))

# Enter the value of y
y = int(input("Enter the value of y: "))

# Compute the value of the algebraic expression
result = (x**2) + (3 * x * y) + (3 * (x * (y**2))) + (y**2)

# Print the result of the computation
print("Result of the expression:", result)
