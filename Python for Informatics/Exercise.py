# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:54:07 2016

@author: geyizhe
"""

# Exercise 7.1
filename = str(input('Enter a file name: '))
fhand = open(filename)
for line in fhand:
    upperLine = line.upper()
    print(upperLine)

# Exercise 7.2
filename = str(input('Enter a file name: '))
fhand = open(filename)
total = 0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        startpos = line.find(" ")
        number = float(line[startpos+1:len(line)])        
    total += number
    count += 1
print("Average span confidence:", total/count)

# Exercise 7.4
try:
    filename = str(input("Enter a file name: "))
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        fhand = open(filename)
        count = 0
        for line in fhand:
            count+=1
        print("There were", count, "subject lines in", filename)
except:
    print("File cannot be opened:", filename)
    
# Chapter 8
# In-book Exercise 1
numlist = []
while True:
    try:
        number = input("Enter a number: ")
        if number == "done":
            break
        else:
            number = float(number)
    except:
        print("invalid input!")
        continue
        
    numlist.append(number)
average = sum(numlist)/len(numlist)
print(average)

# In-book Exercise 2
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 3:
            print(words[2])
    
# Exercise 8.1
def chop(t):
    t.pop(0)
    t.pop()
    return None

def middle(t):
    return t[1:(len(t)-1)]
    
# Exercise 8.2
fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split(' ')
    if words[0] != 'From': continue
    print(words[2])
    
# Exercise 8.4
fhand = open('romeo.txt')
s = []
for line in fhand:
    line = line.rstrip()
    words = line.split(' ')
    for word in words:
        if word not in s: s.append(word)
s.sort()
print(s)

# Exercise 8.5
filename = str(input('Enter a file name: '))
count = 0
fhand = open(filename)
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        count += 1
        words = line.split()
        print(words[1])
print('There were',count,'lines in the file with From as the first word')

# Exercise 8.6
s = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    number = float(number)
    s.append(number)
print('Maximum: ', max(s))
print('Minimun: ', min(s))

# Chapter 9
# In-book Exercise 1
sentence = 'banana and apple'
s = {}
for word in sentence:
    if word not in s.keys():
        s[word] = 1
    else:
        s[word] += 1

# In-book Exercise 2
sentence = 'banana and apple'
s = {}
for word in sentence:
    s[word] = s.get(word, 0)+1

# In-book Exercise 3
fhand = open('romeo.txt')
s = {}
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        s[word] = s.get(word, 0) + 1
        
# In-book Exercise 4
ks = list(s.keys())
ks.sort()
for key in ks:
    print(key, s[key])
    
# Exercise 9.2
filename = str(input('Enter a file name: '))
fhand = open(filename)

d = {}
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split(' ')
    if len(words) < 3: continue
    d[words[2]] = d.get(words[2], 0) + 1
print(d)

# Exercise 9.3
filename = str(input('Enter a filename: '))
fhand = open(filename)
d = {}

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 2: continue
    d[words[1]] = d.get(words[1],0) + 1
print(d)

# Exercise 9.4
filename = str(input('Enter a filename: '))
fhand = open(filename)
d = {}

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    if len(words) < 2: continue
    d[words[1]] = d.get(words[1],0) + 1
    
keys = list(d.keys())
for i in range(len(keys)-1):
    if d[keys[i+1]] > d[keys[i]]:
        largest = [keys[i+1], d[keys[i+1]]]
    else:
        largest = [keys[i], d[keys[i]]]
print(largest[0], largest[1])

# Exercise 9.5
filename = str(input('Enter a file name: '))
fhand = open(filename)
d = {}

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    words = line.split()
    email = words[1]
    startpos = email.find('@')
    domain = email[startpos+1:len(email)]
    d[domain] = d.get(domain, 0) + 1
print(d)

# Chapter 10
# In-book Exercise 1
txt = 'but soft what light in yonder window breaks'
words = txt.split(' ')
l = []
for w in words:
    l.append((len(w), w))
l.sort(reverse=True)

od = []
for length, word in l:
    od.append(word)
print(od)

# In-book Exercise 2
import string
fhand = open('romeo-full.txt')
d = {}
l = []
for line in fhand:
    line = line.rstrip()
    line = line.lower()
    if len(line) == 0: continue
    dictable = str.maketrans({key:None for key in string.punctuation})
    line = line.translate(dictable)
    words = line.split(' ')
    for word in words:
        d[word] = d.get(word, 0)+1
for word, count in d.items():
    l.append((count, word))
    l.sort(reverse=True)
for word, count in l[:10]:
    print(word, count)
    
# Exercise 10.1
d = {}
filename = str(input('Enter a file name: '))
fhand = open(filename)
for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    address = words[1]
    d[address] = d.get(address, 0) + 1

l = []
for address, count in d.items():
    l.append((count, address))
    
l.sort(reverse = True)
for count, address in [l[0]]:
    print(address, count)
    
# Exercise 10.2
d = {}
l = []
filename = str(input('Enter a file name: '))
fhand = open(filename)
for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split()
    hms = words[5].split(':')
    d[hms[0]] = d.get(hms[0], 0) + 1
for hour, count in d.items():
    l.append((hour,count))
l.sort()
for hour, count in l:
    print(hour, count)
    
# Exercise 10.3
import string
fhand = open('romeo-full.txt')

w = {}
l = []

for line in fhand:
    line = line.rstrip()
    if line == '': continue
    line = line.lower()
    transtable = str.maketrans({key:None for key in string.punctuation})
    line = line.translate(transtable)
    words = line.split(' ')
    for word in words:
        for char in word:
            w[char] = w.get(char, 0)+1
    
for char, count in w.items():
    l.append((char, count))
l.sort()

for char, count in l:
    print(char, count)
    
# Chapter 11
# In-book Exercise
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    print(line)

fhand = open('mbox-short.txt')
text = fhand.read()
emails = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', text)

numbers = re.findall('X\S*: ([0-9.]+)', text)

nums = re.findall('Details: \S+=([0-9]+)', text)

hours = re.findall('From .* ([0-9][0-9]):', text)    

# Exercise 11.1
import re
regex = str(input('Enter a regular expression: '))
fhand = open('mbox.txt')
count = 0
for line in fhand:
    line = re.findall(regex, line)
    if line != []: count += 1
print('mbox.txt had', count, 'lines that matched', regex)

# Exercise 11.2
import re
filename = str(input('Enter file: '))
fhand = open(filename)

l = []
for line in fhand:
    line = re.findall('New Revision: ([0-9]+)', line)
    if len(line) > 0:
        l.append(float(line[0]))
sum(l)/len(l)