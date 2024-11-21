#1. Write a Python program that prints all even numbers between 1 and 20 using a for loop
for even_numbers in range(2,20,2):
# #here inside range function first no denotes starting,
# #second denotes end and
# #third denotes the interval
  print(even_numbers,end=' ')

#Alternativey:
for even in range(1,20):
	if even % 2 == 0:
		print(even)
#for even numbers between 1-20
def evenNumbers():
    for even in range(2,20,2):
      print(even)
evenNumbers()

# using list comprehension
evenNumbers = [even for even in range(1,20) if even % 2 == 0]
print(evenNumbers)



#2. Use a while loop to ask the user to input a number until they provide a number greater than 10
num = 0
while num <= 10:
     num = int(input('Enter a number greater than 10: '))
     if num <= 10:
          print('Number should be greater than 10. Try again!')
     else:
          print('Congratulations! You entered a number greater than 10:',num)

#3. Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops
for num in range(1,6):
     print(f'\nMultiplication Table for {num}\t')
     for multiplier in range(1,11):
          result = num * multiplier
          print(f"{num}*{multiplier} = {result}")
          print()

#4. Given a list of integers, [4,7,2,9,12,15], write a program using a for loop  to find the sum of all odd numbers and print the result.
          # Python program to print odd Numbers in a List

# list of numbers
list = [4, 7, 2, 9, 12, 15]
sumOfOddNumbers = 0

# iterating each number in list
for num in list:

    # checking condition
    if num % 2 != 0:
     sumOfOddNumbers+=num
     print(f'Sum of odd numbers:{sumOfOddNumbers }')




     

          
