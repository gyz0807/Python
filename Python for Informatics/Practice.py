# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:55:13 2016

@author: geyizhe
"""

#################################### Random
import random as rd
# random
for i in range(3):
    x = rd.random()
    print(x)
'''
0.7603169362142701
0.8470654731471368
0.9591835042637695
'''

# randint
for i in range(3):
    x = rd.randint(5, 10)
    print(x)
'''
9
8
10
'''

# choice
x = [1, 2, 3]
rd.choice(x)
'''
2
'''

###################################### dir(), help()
# shows the list of methods available for an object
dir(x)
help(x.append)

###################################### string
camels = 42
'%d' % camels

# %d integer, %g floating, %s string
'in %d years, I have spotted %d %s' % (3, 2, 'UFOs')

def find_num(string):
    spacepos = string.find(' ')
    return float(string[spacepos+1:len(string)])

###################################### read and write
# open(): opens a document as a file handle, but does not 
# contain any data
fhand = open('mbox.txt')

count = 0
for line in fhand:
    count += 1
print(count)

# fhand.read(): if you know the file is small compare to your
# memory, you can use read() method on the file handle
inp = fhand.read()
len(inp)

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        
# exit() terminate the programs

# write()
fout = open('output.txt', 'w') # generate the file
line = 'kjdw'
fout.write(line)
fout.close()

###################################### List
numbers = [1,2,3,4]
numbers * 2 # [2, 4, 6, 8, 2, 4, 6, 8]
numbers + numbers # [2, 4, 6, 8, 2, 4, 6, 8]
numbers.append([1,2]) # [1, 2, 3, 4, [1, 2]]
numbers.extend([1,2]) # [1, 2, 3, 4, 1, 2]
numbers.sort() # [1, 1, 1, 2, 2, 3, 4]
numbers.pop(6) # [1, 1, 1, 2, 2, 3], delete elements 6, and return the releted value
numbers.pop() # [1, 1, 1, 2, 2], remove the last value, and return the deleted value
del numbers[0] # [1, 1, 2, 2] delete the element with index 0, if you don't need the removed value
del numbers[2:4] # [1, 1]
numbers.remove(2) # remove the element 2 form the list

# parsing list and strings
s = 'pining for the fjords'
t = s.split() # ['pining', 'for', 'the', 'fjords']
s = 'spam-spam-spam'
s.split('-') # ['spam', 'spam', 'spam']
' '.join(t) # 'pining for the fjords', the inverse of split

# aliasing
a = [1,2,3]
b = a # b = [1, 2, 3]
b[0] = 17 # b = [17, 2, 3]
a # a = [17, 2, 3]

###################################### Dictionary
eng2sp = {}
eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
eng2sp.values() # dict_values(['uno', 'tres', 'dos'])
eng2sp.keys() # dict_keys(['one', 'three', 'two'])
eng2sp.get('four', 'none') # if four is in the keys, it returns the value. if not, returns none

# Make transtable and translate
sentence = 'a! Jake, you are great~'
import string
transtable = str.maketrans({key: None for key in string.punctuation})
sentence = sentence.translate(transtable)
print(sentence) # a Jake you are great

###################################### Tuple
t = ('a',) # create a tuple with a single value
t = tuple('geyizhe') # ('g', 'e', 'y', 'i', 'z', 'h', 'e')
t = ('G',)+t[1:] # ('G', 'e', 'y', 'i', 'z', 'h', 'e'), replace tuple with another

# Comparing tuples
(0, 1, 2) < (0, 3, 4) # True

# Assign multiple values at a time
m = ['have', 'fun']
x, y = m # x = 'have', y = 'fun'
x, y = y, x # swap values

# dictionary to tuple
d = {'a':10, 'b':1, 'c':22}
t = list(d.items())
t.sort()

l = []
for name, value in d.items():
    l.append((value, name))
    l.sort(reverse = True)
    
# complex dictionary
directory = {}
directory[('ge', 'yizhe')] = 123 # {('ge', 'yizhe'): 123}

###################################### Regular Expressions        
# Regular Expression:
# . matches any character
# * matches 0 or more characters
# + matches one or more characters
# /S matches a non-whitespace character
# [] indicates a set of multiple acceptable characters we are willing to consider matching
# () in findall(), it indicates the portion of the substring you are interested in
# ^ beginning
# $ end

# Python
# re.search()
# re.findall()

        
###################################### Networked Programs
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
message = 'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'
message = message.encode('utf-8')
mysock.send(message)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data)

mysock.close()

