'''Write a program that asks the user to enter the coefficients a,b and c of a
quadratic equation a*x^2 + bx + c = 0. The program should find out the
values of � which are the solutions to the quadratic equation using the
formula:
x = −b ± √b^2 − 4ac
/
2a
*to check your code, enter the values of a, b and c as 1, 3 and -4
respectively, the results you get should be 1 and -4'''

# Enter the coefficients a, b, and c
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

# Calculate the quadratic (the square root part)
d = ((b ** 2) - (4 * a * c))**0.5

# Calculate the solutions using the quadratic formula
solution1 = (-b + d) / (2*a)
solution2 = (-b - d) / (2*a)

# Print out the solutions
print("The solutions to the quadratic equation are:")
print("Solution 1:", solution1)
print("Solution 2:", solution2)
