#1. Create a dictionary with three key-value pairs representing a student's information: name,age and grade. Print each key-value pair on a new line.
studentInformation = {
    'Name':'Atim Monica',
    'Age': 25,
    'Grade': '14th'
}  
print(f'Student Info: {studentInformation}')
#Accessing each key-value pair on a new line
print("Name:",studentInformation['Name'])
print("Age:",studentInformation['Age'])
print("Grade:",studentInformation['Grade'])

# Alternatively:
for key, value in studentInformation.items():
    print(f'{key}: {value}')


#2. Write a function that takes a dictionary of people's names and ages and returns a list of people who are 21 or older.
def findAdults(people):
    return[name for name, age in people.items() if age >= 21]
people = {
        'Alice': 24,
        'Bob': 19,
        'Charlie':30
    }
Adults = findAdults(people)
print("Adults:",Adults)
print(f'Adults: {Adults}')# This function uses a list comprehension to iterate over the key-value pairs in the people dictionary.
# It checks if age is 21 or older and if so, adds the corresponding name to the Adults list.

#3. Given a dictionary representing items in store with their prices, write a program that takes a list of items bought and calculates the total cost.
def calculateTotalCost(prices,itemsBought):
    totalCost = 0
    for item in itemsBought:
        if item in prices:
            totalCost += prices[item]
        else:
            print(f"Item '{item}' not found in prices.")
            return totalCost
prices = {
    'apple': 0.5,
    'banana': 0.3,
    'orange': 0.7
}
itemsBought = ['apple','orange','banana','banana']
totalCost = calculateTotalCost(prices,itemsBought)
print(f'Total cost of items bought: {totalCost}')

#Alternatively:
store = {
    'apple': 0.5,
    'banana': 0.3,
    'orange': 0.7}
itemsBought = ['apple','orange','banana','banana']
totalCost = sum(store[item] for item in itemsBought)
print(f'Total cost: {totalCost}')


#4. Write a program that counts the occurences of each word in a given sentence for eg "Hello world hello"
# Define a function named word_count that takes one argument, 'str'.
def word_count(str):
    # Create an empty dictionary named 'counts' to store word frequencies.
    counts = dict()
    
    # Split the input string 'str' into a list of words using spaces as separators and store it in the 'words' list.
    words = str.split()

    # Iterate through each word in the 'words' list.
    for word in words:
        # Check if the word is already in the 'counts' dictionary.
        if word in counts:
            # If the word is already in the dictionary, increment its frequency by 1.
            counts[word] += 1
        else:
            # If the word is not in the dictionary, add it to the dictionary with a frequency of 1.
            counts[word] = 1

    # Return the 'counts' dictionary, which contains word frequencies.
    return counts

# Call the word_count function with an input sentence and print the results.
print( word_count('Hello world hello'))

#Alternatively:

sentence = 'hello world hello'
words = sentence.split()# splitting sentence into words
word_count = {} #dictionary to store the word counts
for word in words:
    word_count[word] = word_count.get(word,0) +1
    print(f'Word count: {word_count}')
