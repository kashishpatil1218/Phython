# Python 

Python is a high-level, interpreted programming language known for its readability and ease of use. Created by Guido van Rossum and first released in 1991, Python has grown to become one of the most popular programming languages in the world. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.

## Key Features of Python
- **Readable and Maintainable Code:** Python’s clean syntax and indentation make the code easy to read and maintain.
- **Comprehensive Standard Library:** Python comes with a rich standard library that supports many common programming tasks.
- **Interpreted Language:** Python code is executed line by line, which makes debugging easier.
- **Cross-Platform:** Python runs on various platforms including Windows, macOS, and Linux.
- **Dynamic Typing:** Variables in Python do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned.
- **Community Support:** Python has a large and active community that contributes to a wealth of third-party modules and frameworks.

## Basic Python Syntax

### Comments
Comments are used to explain code. Python ignores comments.
```python
# This is a single-line comment

"""
This is a 
multi-line comment
"""
```

### Variables
Variables are used to store data.
```python
name = "Alice"
age = 25
```

### Data Types
Common data types include integers, floats, strings, and booleans.
```python
integer_num = 10
float_num = 10.5
string_var = "Hello, World!"
boolean_var = True
```

### Control Structures

#### Conditional Statements
```python
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

#### Loops
```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### Functions
Functions are blocks of reusable code.
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Lists
Lists are used to store multiple items in a single variable.
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

### Dictionaries
Dictionaries store data in key-value pairs.
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person["name"])  # Output: Alice
```

### Importing Modules
Modules are Python files containing Python code. They can define functions, classes, and variables.
```python
import math

print(math.sqrt(16))  # Output: 4.0
```

### Exception Handling
Exceptions are errors detected during execution. Python provides a way to handle these errors using try-except blocks.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

