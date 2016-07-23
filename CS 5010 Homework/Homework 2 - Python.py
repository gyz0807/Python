# -*- coding: utf-8 -*-
"""
Homework 2: Python
@author: Yizhe Ge
"""

# 1. Dictionary basics

## Create a dictionary of 10 key-value pairs.
d = {"one" : 1,
     "two" : 2,
     "three" : 3,
     "four" : 4,
     "five" : 5,
     "six" : 6,
     "seven" : 7,
     "eight" : 8,
     "nine" : 9,
     "ten" : 10} 
## Demonstrate retrieving at least 3 different values
     
val1 = d["one"]
val2 = d["two"]
val3 = d["three"]
## Display each of the results

print(val1)
print(val2)
print(val3)


# 2. Getting user input

## Ask user for their name and two numbers (separately)
name = input("Enter your name: ")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

## Multiply the two numbers
mult = number1 * number2

## Display an output like the following: Hi, <NAME>! Multiplying <NUM1> 
## and <NUM2> is: <RESULT>
## Display the result as a floating-point number (not an integer)
print("Hi, " + name + "!" + " Multiplying " + str(number1) +
      " and " + str(number2) + " is: " + str(mult))
print("\n")

# 3. Converting code to use a while loop

## Rewrite the guessing game using a while loop
answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")

response = input()
numloop = 0
while response != answer:
    
    numloop += 1
    
    if numloop == 1:
        response = input("Sorry. Guess again: ")
    elif numloop == 2:
        response = input("Sorry. One more guess: ")
    else:
        print("Sorry. No more guesses. The answer is " + answer + ".")
        break
    
if numloop < 3:
    print("That is right!")


# 4. Counting each of the vowels

## Using ONE for-loop count the number of each of the vowels in a string
sentence = "are you suggesting coconuts migrate"
vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for i in sentence:
    i = i.lower()
    if i in vowels.keys():
        vowels[i] += 1
        
## Display how many a's, e's, i's, o's, and u's are in the sentence
print(vowels)
    
# 5. Length of all the words in a sentence
## Create a long sentence of words
sentence = 'This is my cat '
sentence += 'That was his dog'
## Put the words into a list
l = sentence.split(" ")
## Use a list comprehension to return each word along with the length of it
lcomp = [(w, len(w)) for w in l]
## Print out each word and its length, but sort by smallest size first
sort = sorted(lcomp, key = lambda x: x[1])
print("\n")
for t in sort:
    print(str(t))
    
# 6. Map-Filter-Reduce examples
def square(number):
    return number * number
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def sum(x, y):
    return x + y

## Rewrite map() function
numbers = [1,2,3]
for i in range(len(numbers)):
    numbers[i] = square(numbers[i])
print(numbers)

## Rewrite filter() function
numbers = list(range(1,11))
numbers = [i for i in numbers if even(i) == True]
print(numbers)

## Rewrite functools.reduce() function
numbers = list(range(1,11))
total = numbers[0]

for i in range(len(numbers)-1):
    total = total + numbers[i+1]
print(total)
    
    
# 7. Classes and Inheritance
class Account:
    
    ## Constructor
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        
    ## create a to-string method
    def __str__(self):
        return "Account number: " + str(self.accountNumber) + "\n" + \
        "Balance: " + str(self.balance)
        
class Checking(Account):
    
    ## Constructor
    def __init__(self, accountNumber, balance, fee):
        Account.__init__(self, accountNumber, balance)
        self.fee = fee
    
    def __str__(self):
        checkingStr = Account.__str__(self)
        checkingStr += "\nAccount type: Checking\n"
        return checkingStr
        
    def getFee(self):
        return self.fee
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amount - self.fee
            
## Create an instance of the Checking class
check1 = Checking(1234, 500, 0.5)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)


# 8. Extra Credit: Write Unit tests for the Account/ Checking classes
import unittest
class checkingTestCase(unittest.TestCase):

    # Test deposit method
    def test_deposit(self):
        checking1 = Checking(4321, 1000, 2)
        checking1.deposit(100)
        self.assertEqual(checking1.balance, 1100)

    # Test withdraw method
    def test_withdraw(self):
        checking2 = Checking(1542, 1000, 2)
        checking2.withdraw(100)
        self.assertEqual(checking2.balance, 898)

    # Test get fee method
    def test_getFee(self):
        checking3 = Checking(984, 1000, 3)
        self.assertEqual(checking3.fee, 3)
        
if __name__== "__main__":
    unittest.main()
