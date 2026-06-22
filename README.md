# Python Programming - Complete Theory Notes

# Table of Contents

1. Introduction to Python
2. History of Python
3. Features of Python
4. Applications of Python
5. Advantages and Limitations
6. Installing Python
7. Python Execution Modes
8. Structure of Python Program
9. Comments
10. Keywords
11. Identifiers
12. Variables
13. Data Types
14. List
15. Tuple
16. Set
17. Dictionary
18. Functions
19. Input and Output
20. Operators
21. Control Statements
22. Loops
23. Modules
24. Exception Handling
25. File Handling
26. Python Libraries
27. Conclusion

---

# Introduction to Python

Python is a high-level, interpreted, general-purpose programming language developed by Guido van Rossum. It is widely used in Web Development, Data Science, Artificial Intelligence, Machine Learning, Automation, Cyber Security, and Software Development.

Python is known for its simple syntax, readability, and ease of learning.

---

# History of Python

* Developed by Guido van Rossum
* Development started in 1989
* Released in 1991
* Named after "Monty Python's Flying Circus"

---

# Features of Python

## Easy to Learn and Use

```python
print("Hello World")
```

## Expressive Language

Requires fewer lines of code.

## Interpreted Language

Executed line-by-line.

## Cross Platform

* Windows
* Linux
* macOS

## Free and Open Source

Available free of cost.

## Extensible

Can integrate with C and C++.

## Large Standard Library

Provides thousands of built-in modules.

## GUI Support

* Tkinter
* PyQt
* Kivy

## Dynamic Memory Allocation

Memory is managed automatically.

## High-Level Language

No need to manage hardware-level details.

---

# Applications of Python

## Web Development

* Django
* Flask
* FastAPI

## Data Science

* NumPy
* Pandas
* Matplotlib

## Machine Learning

* TensorFlow
* Scikit-Learn
* PyTorch

## Artificial Intelligence

* NLP
* Chatbots
* Image Recognition

## Automation

Task automation and scripting.

## Cyber Security

Security testing and analysis.

---

# Advantages of Python

1. Easy to Learn
2. Readable Syntax
3. Huge Community Support
4. Platform Independent
5. Open Source
6. Rapid Development

---

# Limitations of Python

1. Slower than C/C++
2. High Memory Usage
3. Weak Static Typing
4. Not Ideal for System Programming

---

# Installing Python

## Step 1

Download Python from python.org

## Step 2

Install Python

## Step 3

Enable:

```text
✓ Add Python to PATH
```

## Step 4

Verify Installation

```bash
python --version
```

---

# Python Execution Modes

## Interactive Mode

```python
>>> 5 + 5
10
```

## Script Mode

```python
print("Hello Python")
```

Run:

```bash
python program.py
```

---

# Structure of Python Program

```python
# Comment

print("Hello World")
```

Components:

* Comments
* Statements
* Variables
* Functions

---

# Comments

## Single Line Comment

```python
# This is comment
```

## Multi-Line Comment

```python
"""
Multi-line Comment
"""
```

---

# Python Keywords

```python
if
else
for
while
break
continue
return
def
import
True
False
None
```

Display all keywords:

```python
import keyword
print(keyword.kwlist)
```

---

# Identifiers

Identifiers are names given to variables, functions and modules.

Rules:

* Cannot start with number
* Cannot contain special symbols
* Cannot use keywords

Example:

```python
student_name = "Rahul"
```

---

# Variables

Variables are containers for storing data.

```python
name = "Raj"
age = 20
```

---

# Data Types

## Numeric

```python
int
float
complex
```

## Sequence

```python
str
list
tuple
```

## Mapping

```python
dict
```

## Set

```python
set
frozenset
```

## Boolean

```python
bool
```

---

# List in Python

## Definition

A List is an ordered, mutable collection of items.

```python
fruits = ["Apple", "Banana", "Mango"]
```

## Characteristics

* Ordered
* Mutable
* Allows Duplicates
* Supports Multiple Data Types

## Important Methods

```python
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
```

Example:

```python
fruits.append("Orange")
fruits.remove("Banana")
```

---

# Tuple in Python

## Definition

Tuple is an ordered and immutable collection.

```python
colors = ("Red", "Green", "Blue")
```

## Characteristics

* Ordered
* Immutable
* Allows Duplicates

## Methods

```python
count()
index()
```

---

# Set in Python

## Definition

Set is an unordered collection of unique elements.

```python
numbers = {1,2,3,4}
```

## Characteristics

* Unordered
* Mutable
* No Duplicates

## Methods

```python
add()
update()
remove()
discard()
pop()
clear()
union()
intersection()
difference()
issubset()
issuperset()
```

---

# Dictionary in Python

## Definition

Dictionary stores data in key-value pairs.

```python
student = {
    "name": "Rahul",
    "age": 20
}
```

## Characteristics

* Ordered
* Mutable
* Unique Keys

## Methods

```python
keys()
values()
items()
get()
update()
pop()
popitem()
clear()
copy()
setdefault()
```

---

# Functions in Python

## Definition

A function is a reusable block of code.

```python
def greet():
    print("Hello")
```

Call Function:

```python
greet()
```

## Function with Parameters

```python
def greet(name):
    print(name)
```

## Return Statement

```python
def add(a,b):
    return a+b
```

## Types of Functions

### Built-in Functions

```python
print()
input()
len()
sum()
max()
min()
type()
```

### User Defined Functions

```python
def square(n):
    return n*n
```

### Lambda Function

```python
square = lambda x: x*x
```

## Function Arguments

### Positional Arguments

```python
add(10,20)
```

### Keyword Arguments

```python
add(a=10,b=20)
```

### Default Arguments

```python
def greet(name="Guest"):
    print(name)
```

### Variable Length Arguments

```python
def total(*num):
    print(sum(num))
```

## Recursion

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

---

# Input and Output

## Input

```python
name = input("Enter Name: ")
```

## Output

```python
print(name)
```

---

# Operators

## Arithmetic Operators

```python
+
-
*
/
%
**
//
```

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

## Logical Operators

```python
and
or
not
```

## Assignment Operators

```python
=
+=
-=
*=
/=
```

---

# Control Statements

```python
if
if-else
if-elif-else
```

Example:

```python
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# Loops

## For Loop

```python
for i in range(5):
    print(i)
```

## While Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

# Modules

```python
import math

print(math.sqrt(25))
```

Popular Modules:

* math
* random
* datetime
* os
* sys

---

# Exception Handling

```python
try:
    x = 10/0
except ZeroDivisionError:
    print("Error")
```

---

# File Handling

## Writing File

```python
file = open("data.txt","w")
file.write("Hello")
file.close()
```

## Reading File

```python
file = open("data.txt","r")
print(file.read())
file.close()
```

---

# Python Libraries

* NumPy
* Pandas
* Matplotlib
* TensorFlow
* OpenCV
* Requests

---

# Built-in Collection Functions

```python
len()
max()
min()
sum()
sorted()
list()
tuple()
set()
dict()
```

---

# Conclusion

Python is one of the most popular programming languages because of its simplicity, readability, vast ecosystem, and wide range of applications. It is suitable for beginners as well as professional developers and is used in Web Development, Automation, Data Science, Machine Learning, Artificial Intelligence, and many other domains.
