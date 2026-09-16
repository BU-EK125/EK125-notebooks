"""
================================================================================
EK125 — Class 14: Scope, Argument Passing, and Copying
Group Practice Problems - SOLUTIONS
Spring 2026

INSTRUCTOR NOTES:
- This is IDE TRANSITION DAY - expect things to go slowly!
- Students are using VS Code for the first time
- Build in extra time for technical issues
- Emphasize: NO GLOBAL VARIABLES (zero credit!)
- Common issues: Forgetting to save, not knowing how to run code
- Estimated time: 55 minutes (may need adjustment based on tech setup)
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Understanding Local Scope
# ==============================================================================
"""
What will this code print? Predict first, then run it.
Explain why it produces this output.
"""

def test_scope():
    x = 10
    print(f"Inside function: x = {x}")

x = 5
print(f"Before function: x = {x}")
test_scope()
print(f"After function: x = {x}")

# SOLUTION - Prediction:
# Before function: x = 5
# Inside function: x = 10
# After function: x = 5

# SOLUTION - Explanation:
# The x inside test_scope() is a LOCAL variable that only exists inside
# the function. It doesn't affect the x in the main code (global scope).
# When the function ends, the local x is destroyed, and we're back to using
# the global x, which never changed.

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 2: Modifying Lists (Mutable Arguments)
# ==============================================================================
"""
Predict what will happen when we run this code.
Then modify the function to NOT change the original list.
"""

def add_item(my_list, item):
    """Add an item to the list."""
    my_list.append(item)
    return my_list

# Test it
original = [1, 2, 3]
print(f"Original list: {original}")
result = add_item(original, 4)
print(f"Returned list: {result}")
print(f"Original after function: {original}")

# SOLUTION - Why did the original list change?
# Lists are MUTABLE objects. When we pass a list to a function, we're
# passing a reference to the same list object in memory, not a copy.
# So when the function modifies the list, it modifies the original.
# This is called "pass by reference" for mutable objects.

# SOLUTION - Fixed version that doesn't modify original:
def add_item_safe(my_list, item):
    """Add an item to a COPY of the list."""
    new_list = my_list.copy()  # Create a copy first!
    new_list.append(item)
    return new_list

# Test fixed version
original2 = [1, 2, 3]
print(f"\nOriginal list: {original2}")
result2 = add_item_safe(original2, 4)
print(f"Returned list: {result2}")
print(f"Original after function: {original2}")  # Unchanged!

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 3: Shallow vs Deep Copy
# ==============================================================================
"""
Create a nested list and demonstrate the difference between
shallow copy and deep copy.

You'll need to import the copy module!
"""

import copy

# Original nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# SOLUTION: Create a shallow copy
shallow = copy.copy(matrix)
# or: shallow = matrix.copy()

# SOLUTION: Create a deep copy
deep = copy.deepcopy(matrix)

# SOLUTION: Modify the original (change the first element to 999)
matrix[0][0] = 999

# SOLUTION: Print all three and observe what changed
print("Original matrix:", matrix)
print("Shallow copy:", shallow)  # ALSO changed!
print("Deep copy:", deep)        # Did NOT change

# SOLUTION - Explanation:
# SHALLOW COPY copies the outer list, but the inner lists are still
# references to the same objects. So changing matrix[0][0] affects both
# the original and the shallow copy.
#
# DEEP COPY recursively copies everything, creating completely independent
# nested structures. Changes to the original don't affect the deep copy.

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 4: Avoiding Global Variables
# ==============================================================================
"""
This code uses a global variable (BAD PRACTICE!).
Rewrite it to use function parameters instead.

CRITICAL: We NEVER use global variables in this course - zero credit if you do!
"""

# Bad code with global variable:
total = 0  # Global variable - BAD!

def add_bad(x):
    """Bad function that uses global variable."""
    global total  # Using global - BAD!
    total += x
    return total

# SOLUTION: Better version without global variables
def add_good(current_total, value):
    """
    Add a value to the current total.
    
    Parameters:
        current_total (int/float): The current total
        value (int/float): Value to add
    
    Returns:
        int/float: New total
    """
    return current_total + value

# Test the good version:
my_total = 0
my_total = add_good(my_total, 5)
my_total = add_good(my_total, 3)
my_total = add_good(my_total, 7)
print(f"Total: {my_total}")  # Should print 15

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 5: Multiple Return Values and Scope
# ==============================================================================
"""
Write a function that takes a list of numbers and returns THREE values:
- The minimum value
- The maximum value  
- The average

Do NOT use the built-in min(), max(), or sum() functions.
Write your own logic using loops!

Test with: [23, 5, 67, 12, 89, 34, 56, 8]
"""

def analyze_list(numbers):
    """
    Analyze a list of numbers.
    
    Parameters:
        numbers (list): List of numbers to analyze
    
    Returns:
        tuple: (minimum, maximum, average)
    """
    # SOLUTION:
    if not numbers:  # Handle empty list
        return None, None, None
    
    # Find minimum
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    
    # Find maximum
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    
    # Calculate average
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    
    return minimum, maximum, average

# Test the function
test_nums = [23, 5, 67, 12, 89, 34, 56, 8]
min_val, max_val, avg_val = analyze_list(test_nums)
print(f"Numbers: {test_nums}")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"Average: {avg_val:.2f}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 6: Student Grade Tracker
# ==============================================================================
"""
Create a grade tracking system that demonstrates proper use of copying.

Write two functions:

1. calculate_curved_grades(grades, curve_percent)
   - Takes a list of grades and a curve percentage (e.g., 5 for 5%)
   - Returns a NEW list with curved grades
   - Does NOT modify the original list
   - Cap grades at 100

2. drop_lowest_grade(grades)
   - Takes a list of grades
   - Returns a NEW list with the lowest grade removed
   - Does NOT modify the original list

Test both functions and verify the original list is unchanged!
"""

def calculate_curved_grades(grades, curve_percent):
    """
    Apply a curve to grades without modifying the original list.
    
    Parameters:
        grades (list): List of grade values
        curve_percent (float): Percentage to add (e.g., 5 for 5%)
    
    Returns:
        list: New list with curved grades (capped at 100)
    """
    # SOLUTION:
    curved = []
    for grade in grades:
        curved_grade = grade + curve_percent
        # Cap at 100
        if curved_grade > 100:
            curved_grade = 100
        curved.append(curved_grade)
    return curved

def drop_lowest_grade(grades):
    """
    Remove the lowest grade without modifying the original list.
    
    Parameters:
        grades (list): List of grade values
    
    Returns:
        list: New list with lowest grade removed
    """
    # SOLUTION:
    # Make a copy first!
    new_grades = grades.copy()
    
    # Find the minimum
    lowest = new_grades[0]
    for grade in new_grades:
        if grade < lowest:
            lowest = grade
    
    # Remove it (remove() removes first occurrence)
    new_grades.remove(lowest)
    
    return new_grades

# Test the functions
original_grades = [78, 85, 92, 68, 88, 95]
print(f"Original grades: {original_grades}")

curved = calculate_curved_grades(original_grades, 5)
print(f"Curved grades: {curved}")
print(f"Original after curving: {original_grades}")  # Should be unchanged

dropped = drop_lowest_grade(original_grades)
print(f"After dropping lowest: {dropped}")
print(f"Original after dropping: {original_grades}")  # Should be unchanged

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 7: Nested Scope Challenge
# ==============================================================================
"""
Trace through this code carefully. Predict what it will print,
then run it to verify.

This demonstrates nested function scope!
"""

def outer():
    x = "outer"
    
    def inner():
        x = "inner"
        print(f"In inner: {x}")
    
    inner()
    print(f"In outer: {x}")

x = "global"
print(f"Global: {x}")
outer()
print(f"After outer: {x}")

# SOLUTION - Trace:
# Output will be:
# Global: global
# In inner: inner
# In outer: outer
# After outer: global
#
# Explanation:
# - Global x = "global" exists at module level
# - When outer() is called, it creates its own local x = "outer"
# - When inner() is called, it creates its own local x = "inner"
# - Each function sees its own local x, not the outer ones
# - After inner() ends, we're back in outer() with x = "outer"
# - After outer() ends, we're back to global x = "global"

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 8: Deep Copy with Dictionaries (Challenge)
# ==============================================================================
"""
You're managing student data where each student is represented as a dictionary
with a list of quiz scores.

Demonstrate the difference between shallow and deep copy with this structure!
"""

import copy

# Original data
students = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [78, 82, 80]},
    {'name': 'Charlie', 'scores': [92, 88, 95]}
]

# SOLUTION: Create a shallow copy
shallow = copy.copy(students)
# or: shallow = students.copy()

# SOLUTION: Create a deep copy
deep = copy.deepcopy(students)

# SOLUTION: Modify Alice's first score in the original to 100
students[0]['scores'][0] = 100

# SOLUTION: Print all three versions
print("Original:", students)
print("Shallow:", shallow)  # ALSO changed!
print("Deep:", deep)        # Did NOT change

# SOLUTION - Explanation:
# SHALLOW COPY: Copies the outer list, but each dictionary and the lists
# inside those dictionaries are still references to the same objects.
# So changing students[0]['scores'][0] affects both original and shallow.
#
# DEEP COPY: Recursively copies everything - the list, the dictionaries,
# and the lists inside the dictionaries. Completely independent!

print("\n" + "="*60 + "\n")


# ==============================================================================
# TEACHING NOTES
# ==============================================================================
"""
COMMON STUDENT MISTAKES:

1. SCOPE:
   - Using global variables (automatic zero!)
   - Thinking function parameters modify outer variables
   - Not understanding that local variables disappear after function ends

2. MUTABLE ARGUMENTS:
   - Not realizing that lists passed to functions can be modified
   - Forgetting to make a copy before modifying
   - Using = instead of .copy()

3. SHALLOW VS DEEP COPY:
   - Not understanding the difference
   - Using shallow copy for nested structures
   - Forgetting to import copy module for deep copy

4. IDE TRANSITION:
   - Forgetting to save before running
   - Not knowing where to look for output (terminal)
   - Getting lost in file structure
   - Not understanding how to run .py files

GRADING EMPHASIS:
- Zero credit for ANY use of global variables
- Must demonstrate understanding of mutable vs immutable
- Must properly use .copy() or copy.deepcopy()
- Functions must not modify arguments unless explicitly intended

PACING FOR TODAY:
- First 30-35 minutes: IDE setup and walkthrough
- 5 minutes: IPP (on paper)
- 45-50 minutes: GPP work
- Be flexible - this is a transition day!

TIME ESTIMATES BY PROBLEM:
- Problems 1-2: 10 minutes (foundational)
- Problems 3-4: 15 minutes (core concepts)
- Problems 5-6: 20 minutes (application)
- Problems 7-8: 10 minutes (challenge/optional)

STUDENT SUPPORT:
- Walk around constantly
- Check both IDE usage AND content understanding
- Remind to save frequently
- Celebrate small wins with VS Code!
"""
