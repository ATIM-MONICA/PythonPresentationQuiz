#1. Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ['Apples', 'Bananas', 'Blueberries', 'Cherries', 'Grapes']
for fruit in fruits:
  print(fruit)
#2. Write a function that takes a list of numbers and returns a new list  with each number squared. example [1,2,3] and should be [1,4,9].
# Define a function named 'squareNumbers' that generates a list of squares of numbers from 1 to 20
def squareNumbers():
    # Create an empty list 'l'
    x = list()
    
    # Iterate through numbers from 1 to 20 (inclusive)
    for i in range(1, 21):
        # Calculate the square of 'i' and append it to the list 'l'
        x.append(i**2)
    
    # Print the list containing squares of numbers from 1 to 20
    print(x)

# Call the 'squareNumbers' function to generate and print the list of squares
squareNumbers() 

#Alternatively:
def squareNumbers(numbers):
    return[number ** 2 for number in numbers]
print(squareNumbers([1,2,3]))

#3. Write a python program that takes two lists, list1 =  [1,2,3]and list2 = [4,5,6], and combines them into a single list, combined = [1,4,2,5,3,6].
list1 = [1, 2,3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)

#Alternatively:
list1 = [1, 2,3]
list2 = [4, 5, 6]
combined = []
for number in range(len(list1)):
    combined.append(list1[number])
    combined.append(list2[number])
    print(combined)

#4. Given a list of numbers, [3,1,4,1,5,9,2], write a program to find and print two largest numners in the list without using  the max() function
# def find_second_largest(numbers):
#     largest = float('-inf')
#     second_largest = float('-inf')
    
#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#             return largest
#         elif num > second_largest and num != largest:
#             second_largest = num
    
#     return second_largest

# # Example usage
# numbers = [3,1,4,1,5,9,2]
# second_largest = find_second_largest(numbers)
# print("The second largest number is:", second_largest)
# numbers = [3,1,4,1,5,9,2]
# largest = find_second_largest(numbers)
# print("The largest number is:", largest)

# # vals = [3,4,5]
# # twoLargest = sorted(vals)
numbers = [3,1,4,1,5,9,2]
# Initialize the 2 variables to hold the 2 largest numbers
largest = float()
second_largest = float()
#iterate through the list to find the 2 largest numbers
for number in numbers:
    if number > largest:
        second_largest = largest #Update the second largest
        largest = number # update  the largest
    elif number > second_largest:
        second_largest = number # update only the second largest
print("The largest number is:", largest)
print("The second largest number is:", second_largest)