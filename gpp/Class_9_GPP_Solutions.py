"""
================================================================================
EK125 Group Practice Problems - Class 9
Getting Comfortable with PyCharm

NOTE: Each problem below would normally be its own .py file. They are combined
here into one file for easier reference.
================================================================================
"""


# ==============================================================================
# PROBLEM 1 SOLUTION: greeting.py
# ==============================================================================

name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hi {name}! In 10 years you will be {int(age) + 10} years old.")


# ==============================================================================
# PROBLEM 2 SOLUTION: calculator.py
# ==============================================================================

print("=== Simple Calculator ===")
print("Operations: add, multiply, quit")

while True:
    operation = input("\nEnter operation (add/multiply/quit): ")

    if operation == "quit":
        print("Goodbye!")
        break
    elif operation == "add" or operation == "multiply":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if operation == "add":
            result = x + y
        else:
            result = x * y

        print(f"Result: {result}")
    else:
        print("Unknown operation. Please try again.")


# ==============================================================================
# PROBLEM 3 SOLUTION: temperature.py
# ==============================================================================

print("=== Temperature Converter ===")
print("Options: C to F, F to C, quit")

while True:
    direction = input("\nEnter conversion (C to F / F to C / quit): ")

    if direction == "quit":
        print("Goodbye!")
        break
    elif direction == "C to F":
        temp = float(input("Enter temperature: "))
        converted = round(temp * 9/5 + 32, 1)
        print(f"{temp} C = {converted} F")
    elif direction == "F to C":
        temp = float(input("Enter temperature: "))
        converted = round((temp - 32) * 5/9, 1)
        print(f"{temp} F = {converted} C")
    else:
        print("Unknown option. Please try again.")


# ==============================================================================
# PROBLEM 4 SOLUTION: guessing_game.py
# ==============================================================================

import random
secret = random.randint(1, 100)
guesses = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("\nEnter your guess: "))
    guesses += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You got it in {guesses} guesses.")
        break


# ==============================================================================
# PROBLEM 5 SOLUTION: bug_hunt.py
# ==============================================================================

# The three bugs were:
#   Bug 1 (Syntax):  "for score in scores" was missing a colon at the end
#   Bug 2 (Runtime): "len(score)" should be "len(scores)" — score is a single
#                     int (the loop variable), not the list
#   Bug 3 (Logic):   The else branch assigned result = "PASS" instead of "FAIL"

scores = [85, 42, 78, 65, 50]
total = 0

for score in scores:
    total = total + score

average = total / len(scores)

if average >= 65:
    result = "PASS"
else:
    result = "FAIL"

print(f"Average: {average}")
print(f"Result: {result}")


# ==============================================================================
# PROBLEM 6 SOLUTION: weather_data.py
# ==============================================================================

temps_f = [45, 52, 48, 61, 55, 37, 42, 58, 63, 50, 47, 59, 64, 53]

# Step 1: Convert to Celsius
temps_c = [round((f - 32) * 5/9, 1) for f in temps_f]
print(f"Celsius: {temps_c}")

# Step 2: Filter warm days (>= 15°C)
warm_days = [t for t in temps_c if t >= 15]
print(f"Warm days: {warm_days}")

# Step 3: Day-to-day changes
changes = [round(temps_c[i+1] - temps_c[i], 1) for i in range(len(temps_c) - 1)]
print(f"Changes: {changes}")


# ==============================================================================
# PROBLEM 7 SOLUTION: collatz.py
# ==============================================================================

# Part A: Single number
n = int(input("Enter a positive integer: "))
sequence = [n]
steps = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    sequence.append(n)
    steps += 1

print(" -> ".join(str(x) for x in sequence))
print(f"Steps: {steps}")

# Part B (Challenge): Find longest sequence from 1 to 100
longest_n = 1
longest_steps = 0

for start in range(1, 101):
    n = start
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    if steps > longest_steps:
        longest_steps = steps
        longest_n = start

print(f"\nLongest sequence: starting number {longest_n} takes {longest_steps} steps")
