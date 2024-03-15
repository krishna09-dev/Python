'''1. Write a program that takes a number N as input and prints the sum of all the numbers from 1 to  N.'''

#taking input from user
a = int(input("Enter the number till where u want sum"))
sum_ = 0

#for loop for adding the numbers
for i in range(1,a+1):
    sum_ += i
    
#printing the total sum
print(f"The sum of numbers from 1 to {a} is: {sum_}")
    
