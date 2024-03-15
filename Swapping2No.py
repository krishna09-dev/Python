'''Write a program that asks the user to enter two numbers a and b. Then
write code to swap the values of a and b, and print them out.'''

# Enter two numbers a and b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Print the values before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values of a and b using a temporary variable
temp = a
a = b
b = temp

# Print the values after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
