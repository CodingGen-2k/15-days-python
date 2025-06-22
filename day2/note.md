# ✅ Day 2: Python Operators & Strings

---

## 🔹 Python Operators

Operators are special symbols used to perform operations on variables and values.

### 1. Arithmetic Operators
Used to perform mathematical operations:

```python
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.33
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000
```

---

### 2. Comparison (Relational) Operators
Compares two values and returns `True` or `False`:

```python
a = 5
b = 7
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

---

### 3. Logical Operators
Used to combine conditional statements:

```python
x = 5
print(x > 3 and x < 10)  # True
print(x < 3 or x > 4)    # True
print(not(x > 3))        # False
```

---

### 4. Assignment Operators
Used to assign values to variables:

```python
x = 10
x += 5  # x = x + 5 → 15
x -= 3  # x = x - 3 → 12
x *= 2  # x = x * 2 → 24
x /= 6  # x = x / 6 → 4.0
x %= 2  # x = x % 2 → 0.0
```

---

### 5. Identity Operators
Checks if two variables refer to the same object:

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True
```

---

### 6. Membership Operators
Checks if a value is in a sequence:

```python
fruits = ['apple', 'banana']
print('apple' in fruits)      # True
print('mango' not in fruits)  # True
```

---

## 🔹 Python Strings

A string is a sequence of characters enclosed in quotes.

```python
name = "Python"
```

---

### 1. String Indexing
Access characters using index (starts from 0):

```python
text = "hello"
print(text[0])  # h
print(text[-1]) # o
```

---

### 2. String Slicing
Extract a portion of the string:

```python
text = "hello world"
print(text[0:5])  # hello
print(text[6:])   # world
print(text[:5])   # hello
```

---

### 3. Common String Methods

```python
s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.lower())       # 'python programming'
print(s.title())       # 'Python Programming'
print(s.strip())       # Removes whitespace
print(s.replace("python", "java"))  # 'java programming'
print(s.find("pro"))   # 7
```

---

### 4. String Formatting

#### a) f-strings (Python 3.6+)

```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

#### b) format() method

```python
print("My name is {} and I am {} years old.".format("Bob", 30))
```

---

## ✅ Practice Tips
- Try all operators with different data types.
- Practice slicing and formatting strings.
- Experiment with string methods on your own strings.

---
