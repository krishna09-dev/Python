'''A Fibonacci sequence is characterized by the fact
that every number after the first two is the sum
of the two preceding ones. By definition, the
first two numbers in the Fibonacci sequence are
1 and 1.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55
Write a program that generates the first N
numbers of the Fibonacci sequence and prints
them out. N should be taken as input from the
user. '''

#Creating empty list
array = [1,1]

#taking data from user
a = int(input("Enter the number of elemts u want to keep in list"))

#for loop for adding element to the list given by user
for i in range (a):#range(2,n) no need for if else
    if i==1 or i==2:
        continue
    else:
        next_number = array[i-1] + array[i-2]
        array.append(next_number)
        
#printing the series from list
print(array)
