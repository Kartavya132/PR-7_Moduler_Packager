# 🛠️ Omni Media Tool

A Python-based command-line utility that combines multiple useful tools into one application. It provides 📅 date & time utilities, ➗ mathematical calculations, 🎲 random data generation, 🆔 UUID creation, 📂 file operations, and 🔍 module attribute exploration.

## ✨ Features

* 📅 Date & Time Operations
* ➗ Mathematical Calculations
* 🎲 Random Data Generation
* 🆔 UUID Generator
* 📂 File Operations
* 🔍 Module Attribute Explorer
* 📋 Menu Driven Interface

---

# 🏠 Main Menu

```text
------Main Menu------
1. 📅 Datetime and Time Operations
2. ➗ Mathematical Operations
3. 🎲 Random Data Generator
4. 🆔 Generate Unique ID (UUID)
5. 📂 File Operations
6. 🔍 Attributes Explorer
7. ❌ Exit
```
---
# Project Structure
```text
Moduler_Packager/
│
├── main.py     
└── Package/    
    ├── __init__.py
    ├── menu.py   
    ├── datetime_tools.py  
    ├── math_tools.py      
    ├── random_tools.py    
    ├── uuid_tool.py 
    ├── file_tools.py
    └── attributes.py
```
---

# 📅 Date & Time Operations

```text
1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown timer
6. Back to Main Menu
```

## 🕒 1. Display Current Date & Time

### Input

```text
1
```

### Output

```text
Current Date and time is 2025-06-20 14:30:10.123456
```

---

## 📆 2. Calculate Difference Between Two Dates

### Input

```text
2
Enter the first date (YYYY-MM-DD): 2025-01-01
Enter the second date (YYYY-MM-DD): 2025-01-15
```

### Output

```text
The difference :: 14 day/s
```

### ❌ Invalid Input

```text
Enter the first date (YYYY-MM-DD): abc
Enter the second date (YYYY-MM-DD): xyz
```

### Output

```text
Invalid Date
```

---

## 📝 3. Format Date

### Input

```text
3
Enter the date (YYYY-MM-DD): 2025-06-20
Enter the format of date(EX: %d-%m-%Y): %d/%m/%Y
```

### Output

```text
Formatted date :: 20/06/2025
```

### ❌ Invalid Input

```text
You Enter invalid format!!
```

---

## ⏱️ 4. Stopwatch

### Input

```text
4
Press Enter to Start
Press Enter to Stop
```

### Output

```text
The stopped: 0:00:12.456789
```

---

## ⏳ 5. Countdown Timer

### Input

```text
5
Enter the duration(minutes): 1
```

### Output

```text
1 min is passed
```

### ❌ Invalid Input

```text
Invalid Input
```

---

# ➗ Mathematical Operations

```text
1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Operations
4. Area of Geometric Shapes
5. Back to Main Menu
```

---

## 🔢 1. Factorial

### Input

```text
1
Enter the number : 5
```

### Output

```text
The factorial of 5 is 120
```

### ❌ Invalid Input

```text
Invalid Input
```

---

## 💰 2. Compound Interest

### Formula Used

```text
A = P(1 + r/100)^t
```

### Input

```text
2
Enter the principal amount : 1000
Enter the rate of interest : 5
Enter the duration in years : 2
```

### Output

```text
The Total Amount is $1102.5
```

### ❌ Invalid Input

```text
Invalid Input!!
```

---

## 📐 3. Trigonometric Operations

### 🔹 Sin

#### Input

```text
s
Enter the angle : 30
```

#### Output

```text
Sin 0.5235987755982988 is 0.5
```

### 🔹 Cos

#### Input

```text
c
Enter the angle : 60
```

#### Output

```text
Cos 1.0471975511965976 is 0.5
```

### 🔹 Tan

#### Input

```text
t
Enter the angle : 45
```

#### Output

```text
Tan 0.7853981633974483 is 1.0
```

### ❌ Invalid Input

```text
Invalid Input!!
```

---

## 📏 4. Area of Geometric Shapes

### ⚪ Circle

#### Input

```text
c
Enter the radius (cm): 5
```

#### Output

```text
The area is 78.53981633974483
```

---

### 🔺 Triangle (Heron's Formula)

#### Input

```text
t
Enter first side: 3
Enter second side: 4
Enter third side: 5
```

#### Output

```text
The area is 6.0cm
```

---

### ▭ Rectangle

#### Input

```text
r
Enter length : 10
Enter breadth : 5
```

#### Output

```text
The area is 50
```

---

### ◼️ Square

#### Input

```text
s
Enter side : 4
```

#### Output

```text
The area is 16
```

### ❌ Invalid Choice

```text
Invalid choice!!
```

---

# 🎲 Random Data Generator

```text
1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Back to Main Menu
```

---

## 🎯 1. Random Number

### Input

```text
Enter number of digits : 4
```

### Output

```text
The random number is 5832
```

---

## 📋 2. Random List

### Input

```text
Enter length of list : 5
```

### Output

```text
The random generated lists is:
:- 4 7 1 8 2
```

---

## 🔐 3. Random Password

### Input

```text
Enter length of password : 12
```

### Output

```text
The random generated password : Ab#8kP1@Qm2$
```

---

## 📲 4. Random OTP

### Input

```text
Enter length of OTP : 6
```

### Output

```text
The random generated otp : 583291
```

---

## ❌ Possible Invalid Outputs

```text
Invalid Input!!
```

---

# 🆔 UUID Generator

Generates a Version-4 UUID.

### Input

```text
4
```

### Output

```text
Generate Unique ID ::-
ID:- 550e8400-e29b-41d4-a716-446655440000
Thank you!, Press Enter to continue
```

---

# 📂 File Operations

```text
1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu
```

---

## 📄 1. Create File

### Input

```text
sample.txt
```

### Output

```text
The file is created!!
```

### ⚠️ Existing File

```text
file already exists make new file
```

---

## ✍️ 2. Write to File

### Input

```text
sample.txt
Hello World.This is test data.
```

### File Content

```text
Hello World.
This is test data.
```

### Output

```text
The lines are written
```

---

## 📖 3. Read File

### Input

```text
sample.txt
```

### Output

```text
The lines in file is ::-
Hello World.
This is test data.

All lines is readed
```

### ❌ File Not Found

```text
There si no such file!
```

---

## ➕ 4. Append to File

### Input

```text
sample.txt
New line added.
```

### Output

```text
The lines added
```

### Updated File

```text
Hello World.
This is test data.
New line added.
```

---

# 🔍 Attributes Explorer

Displays available attributes of selected modules.

### ✅ Supported Modules

* 📐 math
* 🎲 random
* 📅 datetime
* 🆔 uuid
* ⚙️ sys

### Input

```text
math
```

### Output

```text
The Attributes are :-
[
acos,
acosh,
asin,
...
]
```

### ❌ Invalid Module

```text
Invalid module
```

---

# 🛡️ Error Handling

The application handles:

* ❌ Invalid menu selections
* 📅 Invalid dates
* 🔢 Invalid numeric inputs
* 📂 Missing files
* ⚠️ Existing files
* 🔍 Unsupported modules

### Possible Outputs

```text
Invalid choice
Invalid Input
Invalid Input!!
Invalid Date
Invalid module
There si no such file!
file already exists make new file
```

---

# 📦 Modules Used

```python
import math
import datetime
import random
import uuid
import sys
```
