"""
================================================================================
EK125 — Class 15: Scripts, Comments, and Documentation
Group Practice Problems - SOLUTIONS
Spring 2026

INSTRUCTOR NOTES:
- Second day with VS Code - students should be more comfortable
- Focus today is on PROFESSIONAL CODE PRACTICES
- Emphasize quality over quantity
- This is setting habits for the rest of the semester
- Walk around and check documentation quality, not just correctness
- Estimated time: 55 minutes
================================================================================
"""

# ==============================================================================
# PROBLEM 1: Good Comments vs. Bad Comments
# ==============================================================================
"""
Below are examples of comments. Identify which are GOOD and which are BAD.
Then rewrite the bad ones to be better.

Remember: Good comments explain WHY, not WHAT. They clarify non-obvious logic.
"""

# Example 1:
x = x + 1  # Add 1 to x
# SOLUTION: BAD comment - states the obvious
# Better: No comment needed, or explain WHY we're incrementing

# Example 2:
# Apply 20% curve because this exam was particularly challenging
final_grade = raw_score * 1.20
# SOLUTION: GOOD comment - explains WHY we're using 1.20

# Example 3:
total = sum(numbers)  # Calculate the total of all numbers
# SOLUTION: BAD comment - states the obvious (sum clearly calculates total)
# Better: No comment, or explain WHY we need the total

# Example 4:
# Convert temperature to Celsius for consistency with weather API
temp_c = (temp_f - 32) * 5/9
# SOLUTION: GOOD comment - explains WHY we're converting

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 2: Adding Docstrings to Functions
# ==============================================================================
"""
Below is a function with NO documentation. Add a proper docstring that includes:
- Brief description of what the function does
- Parameters (with types and descriptions)
- Return value (with type and description)
- An example of usage
"""

# SOLUTION: Function with proper docstring
def calculate_final_grade(homework, quizzes, exams):
    """
    Calculate final grade based on homework, quizzes, and exams.
    
    Uses weighted average: 27% homework, 20% quizzes, 30% exams,
    plus 18% class participation (pre-added).
    
    Parameters:
        homework (list): List of homework grades (0-100)
        quizzes (list): List of quiz grades (0-100)
        exams (list): List of exam grades (0-100)
    
    Returns:
        float: Final grade out of 100
    
    Example:
        >>> hw = [85, 90, 88]
        >>> quiz = [78, 82, 85]
        >>> exam = [82, 88]
        >>> calculate_final_grade(hw, quiz, exam)
        83.5
    """
    hw_avg = sum(homework) / len(homework)
    quiz_avg = sum(quizzes) / len(quizzes)
    exam_avg = sum(exams) / len(exams)
    
    final = hw_avg * 0.27 + quiz_avg * 0.20 + exam_avg * 0.30 + 18
    
    return final

# Test the documented function:
hw = [85, 90, 88, 92]
quiz = [78, 82, 85, 80, 88]
exam = [82, 88, 85]

grade = calculate_final_grade(hw, quiz, exam)
print(f"Final grade: {grade:.1f}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 3: Script Organization
# ==============================================================================
"""
Below is messy code. Reorganize it properly using these principles:

1. Module docstring at the top
2. Imports next
3. Constants (if any)
4. Function definitions (with docstrings!)
5. Main program code
6. Use if __name__ == "__main__": pattern
"""

# SOLUTION: Properly organized code
"""
Health and Geometry Calculator Module

This module provides functions for calculating BMI and circle areas.
"""

# Imports
import math

# Constants
PI = 3.14159

# Function definitions
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight / (height ** 2)

def circle_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): Radius of the circle
    
    Returns:
        float: Area of the circle
    """
    return PI * radius ** 2

# Main program
if __name__ == "__main__":
    # Calculate and display BMI
    result = calculate_bmi(70, 1.75)
    print(f"BMI: {result:.1f}")
    
    # Calculate and display circle area
    area = circle_area(5)
    print(f"Area: {area:.2f}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 4: Professional Temperature Converter
# ==============================================================================
"""
Create a COMPLETE, professionally documented temperature conversion script.

Requirements:
1. Module docstring at top explaining what the script does
2. Three functions (each with proper docstrings):
   - celsius_to_fahrenheit(celsius)
   - fahrenheit_to_celsius(fahrenheit)
   - kelvin_to_celsius(kelvin)
3. Each function should:
   - Have a clear, descriptive docstring
   - Include parameter and return descriptions
   - Have an example in the docstring
4. Use the if __name__ == "__main__": pattern
5. Include helpful (not obvious) comments where needed
"""

# SOLUTION: Complete, professional module
"""
Temperature Conversion Module

This module provides functions for converting between different temperature
scales: Celsius, Fahrenheit, and Kelvin.

Common conversions:
- Celsius to Fahrenheit: F = (C * 9/5) + 32
- Fahrenheit to Celsius: C = (F - 32) * 5/9
- Kelvin to Celsius: C = K - 273.15
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius
    
    Returns:
        float: Temperature in degrees Fahrenheit
    
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Parameters:
        fahrenheit (float): Temperature in degrees Fahrenheit
    
    Returns:
        float: Temperature in degrees Celsius
    
    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    
    Parameters:
        kelvin (float): Temperature in Kelvin
    
    Returns:
        float: Temperature in degrees Celsius
    
    Example:
        >>> kelvin_to_celsius(273.15)
        0.0
        >>> kelvin_to_celsius(373.15)
        100.0
    """
    return kelvin - 273.15

def main():
    """Demonstrate temperature conversions."""
    print("Temperature Conversion Examples")
    print("-" * 40)
    
    # Test Celsius to Fahrenheit
    temp_c = 25
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f:.1f}°F")
    
    # Test Fahrenheit to Celsius
    temp_f = 77
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F = {temp_c:.1f}°C")
    
    # Test Kelvin to Celsius
    temp_k = 300
    temp_c = kelvin_to_celsius(temp_k)
    print(f"{temp_k}K = {temp_c:.1f}°C")

if __name__ == "__main__":
    main()

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 5: Code Review - Fix the Documentation
# ==============================================================================
"""
This function has TERRIBLE documentation. Your job:
1. Add a proper docstring
2. Rename variables to be more descriptive
3. Add helpful comments (not obvious ones!)
4. Make it professional!
"""

# BAD VERSION:
def calc(a, b):
    c = []
    for i in a:
        if i > b:
            c.append(i)
    return c

# SOLUTION: Improved version
def filter_above_threshold(numbers, threshold):
    """
    Filter numbers that exceed a specified threshold.
    
    Useful for data cleaning, outlier detection, or selecting values
    above a certain limit.
    
    Parameters:
        numbers (list): List of numeric values to filter
        threshold (float): Minimum value (exclusive) to include
    
    Returns:
        list: Numbers from input list that are greater than threshold
    
    Example:
        >>> filter_above_threshold([10, 25, 30, 15, 40], 20)
        [25, 30, 40]
    """
    filtered_numbers = []
    
    for number in numbers:
        if number > threshold:
            filtered_numbers.append(number)
    
    return filtered_numbers

# Test the improved function:
numbers = [23, 45, 12, 67, 34, 89, 15, 56]
threshold = 40
result = filter_above_threshold(numbers, threshold)
print(f"Numbers above {threshold}: {result}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 6: Creating a Module with if __name__ == "__main__"
# ==============================================================================
"""
Create a GPA calculator module that can be both:
1. Imported and used by other programs
2. Run directly as a script

Your module should include:
- Module docstring
- calculate_gpa(grades, credits) function with proper docstring
- letter_grade(gpa) function with proper docstring
- main() function that demonstrates usage
- if __name__ == "__main__": pattern

GPA Calculation: sum(grade * credit) / sum(credits)

Letter grades:
A: 3.7-4.0, B: 2.7-3.69, C: 1.7-2.69, D: 1.0-1.69, F: <1.0
"""

# SOLUTION: Complete GPA calculator module
"""
GPA Calculator Module

This module provides functions for calculating Grade Point Average (GPA)
and converting numeric GPAs to letter grades.

Can be imported by other programs or run directly as a demonstration.
"""

def calculate_gpa(grades, credits):
    """
    Calculate weighted GPA based on grades and credits.
    
    Parameters:
        grades (list): List of numeric grades (0.0-4.0 scale)
        credits (list): List of credit hours for each course
    
    Returns:
        float: Weighted GPA rounded to 2 decimal places
    
    Example:
        >>> calculate_gpa([4.0, 3.7, 3.3], [3, 4, 3])
        3.72
    """
    if len(grades) != len(credits):
        return None
    
    # Calculate weighted sum of grades
    total_points = 0
    for grade, credit in zip(grades, credits):
        total_points += grade * credit
    
    total_credits = sum(credits)
    
    if total_credits == 0:
        return 0.0
    
    return round(total_points / total_credits, 2)

def letter_grade(gpa):
    """
    Convert numeric GPA to letter grade.
    
    Parameters:
        gpa (float): Numeric GPA (0.0-4.0 scale)
    
    Returns:
        str: Letter grade ('A', 'B', 'C', 'D', or 'F')
    
    Example:
        >>> letter_grade(3.8)
        'A'
        >>> letter_grade(2.9)
        'B'
    """
    if gpa >= 3.7:
        return 'A'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.0:
        return 'D'
    else:
        return 'F'

def main():
    """Demonstrate GPA calculation with example data."""
    print("GPA Calculator Demo")
    print("-" * 40)
    
    # Example student grades
    course_grades = [4.0, 3.7, 3.3, 3.0, 4.0]
    course_credits = [3, 4, 3, 4, 3]
    
    gpa = calculate_gpa(course_grades, credits)
    letter = letter_grade(gpa)
    
    print(f"Grades: {course_grades}")
    print(f"Credits: {course_credits}")
    print(f"GPA: {gpa}")
    print(f"Letter Grade: {letter}")

if __name__ == "__main__":
    main()

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 7: Documentation Best Practices
# ==============================================================================
"""
Write a function called analyze_sensor_data that:
- Takes a list of temperature readings (floats)
- Returns: count, average, min, max, and readings above 75°F

This function must demonstrate ALL of these documentation best practices:
1. Module-level docstring (at the very top of this section)
2. Function docstring with Parameters and Returns sections
3. Example usage in the docstring
4. Helpful comments explaining WHY, not WHAT
5. Clear variable names
6. Proper formatting and structure
"""

# SOLUTION: Exemplary documentation
"""
Sensor Data Analysis Module

Provides functions for analyzing temperature sensor readings,
including statistical analysis and threshold detection.
"""

def analyze_sensor_data(temperature_readings):
    """
    Analyze temperature sensor data and identify high readings.
    
    Provides statistical summary and flags readings above 75°F,
    which may indicate equipment overheating or environmental concerns.
    
    Parameters:
        temperature_readings (list): Temperature values in Fahrenheit
    
    Returns:
        dict: Dictionary containing:
            - 'count' (int): Number of readings
            - 'average' (float): Mean temperature
            - 'min' (float): Lowest temperature
            - 'max' (float): Highest temperature
            - 'above_threshold' (list): Readings above 75°F
    
    Example:
        >>> temps = [68.5, 72.0, 78.3, 65.2, 80.1, 71.8]
        >>> analyze_sensor_data(temps)
        {'count': 6, 'average': 72.65, 'min': 65.2, 'max': 80.1,
         'above_threshold': [78.3, 80.1]}
    """
    # Early return for empty data
    if not temperature_readings:
        return None
    
    # Calculate basic statistics
    count = len(temperature_readings)
    average = sum(temperature_readings) / count
    minimum = min(temperature_readings)
    maximum = max(temperature_readings)
    
    # Identify readings above critical threshold (75°F)
    # This threshold indicates potential overheating concerns
    critical_threshold = 75.0
    above_threshold = []
    
    for reading in temperature_readings:
        if reading > critical_threshold:
            above_threshold.append(reading)
    
    # Return structured results
    return {
        'count': count,
        'average': round(average, 2),
        'min': minimum,
        'max': maximum,
        'above_threshold': above_threshold
    }

# Test the function
test_readings = [68.5, 72.0, 78.3, 65.2, 80.1, 71.8, 76.4]
results = analyze_sensor_data(test_readings)
print("Sensor Data Analysis:")
print(f"  Count: {results['count']}")
print(f"  Average: {results['average']}°F")
print(f"  Range: {results['min']}°F - {results['max']}°F")
print(f"  High readings (>75°F): {results['above_threshold']}")

print("\n" + "="*60 + "\n")


# ==============================================================================
# PROBLEM 8: Understanding the if __name__ == "__main__" Pattern
# ==============================================================================
"""
Explain in your own words:

1. What does if __name__ == "__main__": mean?

SOLUTION:
This checks whether the Python file is being run directly or being imported
as a module by another program. When you run a file directly, Python sets
the special variable __name__ to "__main__". When you import it, __name__
is set to the module's name instead.


2. When does Python set __name__ to "__main__"?

SOLUTION:
When you execute the file directly from the command line or IDE. For example:
- Running: python my_script.py
- Clicking "Run" in VS Code
- Not true when another file does: import my_script


3. Why is this pattern useful?

SOLUTION:
It allows your code to serve two purposes:
- As a reusable module that other programs can import
- As a standalone script that can be run directly
The code inside if __name__ == "__main__": only runs when executed directly,
not when imported. This lets you include test code or demonstrations without
affecting other programs that import your functions.


4. What happens if you DON'T use this pattern?

SOLUTION:
All code at the module level runs immediately when the file is imported.
This can cause problems:
- Test code runs when you just want to import functions
- Output appears when it shouldn't
- Variables are created that you don't need
- Side effects happen unexpectedly
"""

# SOLUTION: Example demonstrating the pattern
"""
Example Calculator Module

Demonstrates the if __name__ == "__main__" pattern.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def main():
    """Run demonstrations of calculator functions."""
    print("Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")

# This only runs when the file is executed directly,
# NOT when it's imported by another program
if __name__ == "__main__":
    main()

# If another program does: import class15_gpp
# Then: add() and multiply() are available, but main() doesn't run

print("\n" + "="*60 + "\n")


# ==============================================================================
# TEACHING NOTES
# ==============================================================================
"""
COMMON STUDENT MISTAKES:

1. COMMENTS:
   - Writing obvious comments that state what the code does
   - No comments at all
   - Too many comments
   - Comments that lie (don't update when code changes)

2. DOCSTRINGS:
   - No docstrings on functions
   - Docstrings that just restate the function name
   - Missing Parameters or Returns sections
   - No examples

3. ORGANIZATION:
   - Random order of imports, functions, and main code
   - Not using if __name__ == "__main__":
   - No module docstring
   - Constants mixed with functions

4. VARIABLE NAMES:
   - Single letters (except in loops)
   - Abbreviations that aren't clear
   - Not descriptive enough

GRADING EMPHASIS:
- All functions must have docstrings
- Comments must explain WHY, not WHAT
- Proper script organization required
- Clear, descriptive variable names
- Must use if __name__ == "__main__": pattern

PACING:
- Problems 1-3: 15 minutes (fundamentals)
- Problems 4-5: 20 minutes (application)
- Problems 6-7: 15 minutes (integration)
- Problem 8: 5 minutes (understanding)
- Total: ~55 minutes

TEACHING EMPHASIS:
- Professional code is about communication
- Future you (and others) will read this code
- Documentation is not optional
- These habits matter for real projects
- This is how industry code looks

STUDENT SUPPORT:
- Show examples of real open-source projects
- Emphasize: this is professional practice
- Remind: exams require clear code too
- Walk around and check documentation quality
"""
