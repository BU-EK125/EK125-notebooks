"""
================================================================================
EK125 Group Practice Problems - Class 9
Getting Comfortable with PyCharm

Work through these problems with your group. For each problem, create a NEW
Python file in your EK125 project (right-click project folder > New > Python
File). Write your code, then run it using the green play button or by
right-clicking in the editor and selecting Run.

REMEMBER:
  - You must use print() to see output — nothing displays automatically!
  - Click inside the Run panel at the bottom to type input when prompted.
  - Run your file often as you write code. Don't wait until the end!
================================================================================
"""


# ==============================================================================
# PROBLEM 1: Greeting Program (~10 minutes)
# ==============================================================================
"""
Create a new file called: greeting.py

Write a program that:
  1. Uses input() to ask the user for their name.
  2. Uses input() to ask the user for their age.
  3. Calculates how old they will be in 10 years.
  4. Prints a greeting that includes their name and their age in 10 years.

Hints:
  - Remember that input() always returns a string. You will need to convert
    the age to an integer using int() before doing math with it.
  - Use an f-string for the final print statement.

Example run (user input shown after the colon):
  What is your name? Alice
  How old are you? 19
  Hi Alice! In 10 years you will be 29 years old.
"""


# ==============================================================================
# PROBLEM 2: Simple Calculator (~15 minutes)
# ==============================================================================
"""
Create a new file called: calculator.py

Write a program that repeatedly asks the user to pick an operation (add,
multiply, or quit), then asks for two numbers and prints the result. The
program should keep running until the user types "quit".

Your program should:
  1. Print a welcome message listing the available operations.
  2. Use a while loop that runs forever (while True).
  3. Inside the loop:
     a. Use input() to ask the user for an operation.
     b. If the operation is "quit", print "Goodbye!" and break out of the loop.
     c. If the operation is "add" or "multiply", ask for two numbers using
        input() and convert them to floats. Compute and print the result.
     d. If the operation is anything else, print "Unknown operation."

Example run:
  === Simple Calculator ===
  Operations: add, multiply, quit

  Enter operation (add/multiply/quit): add
  Enter first number: 10
  Enter second number: 3.5
  Result: 13.5

  Enter operation (add/multiply/quit): multiply
  Enter first number: 4
  Enter second number: 7
  Result: 28.0

  Enter operation (add/multiply/quit): quit
  Goodbye!
"""


# ==============================================================================
# PROBLEM 3: Temperature Converter (~15 minutes)
# ==============================================================================
"""
Create a new file called: temperature.py

Write a program that converts temperatures between Celsius and Fahrenheit.
The program should:
  1. Ask the user which direction to convert: "C to F" or "F to C".
  2. Ask the user for the temperature value.
  3. Perform the conversion and print the result rounded to 1 decimal place.
  4. Repeat until the user types "quit" instead of a conversion direction.

Conversion formulas:
  Fahrenheit = Celsius * 9/5 + 32
  Celsius = (Fahrenheit - 32) * 5/9

Example run:
  === Temperature Converter ===
  Options: C to F, F to C, quit

  Enter conversion (C to F / F to C / quit): C to F
  Enter temperature: 100
  100.0 C = 212.0 F

  Enter conversion (C to F / F to C / quit): F to C
  Enter temperature: 32
  32.0 F = 0.0 C

  Enter conversion (C to F / F to C / quit): quit
  Goodbye!

Hints:
  - Convert the temperature input to a float.
  - Use round(value, 1) to round to 1 decimal place.
  - Compare the user's input string directly: if direction == "C to F"
"""


# ==============================================================================
# PROBLEM 4: Number Guessing Game (~20 minutes)
# ==============================================================================
"""
Create a new file called: guessing_game.py

Write a number guessing game. The program picks a secret number and the user
tries to guess it, getting "Too high" or "Too low" hints after each guess.

Your program should:
  1. Store a secret number in a variable (pick any integer, e.g. 42).
  2. Use a variable to count the number of guesses (start at 0).
  3. Use a while loop that keeps running until the user guesses correctly.
  4. Inside the loop:
     a. Ask the user for their guess and convert it to an integer.
     b. Increment the guess counter.
     c. If the guess is too low, print "Too low! Try again."
     d. If the guess is too high, print "Too high! Try again."
     e. If the guess is correct, print a congratulations message that
        includes how many guesses it took, then break.

Example run (secret number is 42):
  I'm thinking of a number between 1 and 100.

  Enter your guess: 50
  Too high! Try again.

  Enter your guess: 25
  Too low! Try again.

  Enter your guess: 42
  Correct! You got it in 3 guesses.

CHALLENGE (optional): After you get the basic version working, try importing
the random module and using random.randint(1, 100) to pick a truly random
secret number each time:
  import random
  secret = random.randint(1, 100)
"""


# ==============================================================================
# PROBLEM 5: Bug Hunt (~15 minutes)
# ==============================================================================
"""
Create a new file called: bug_hunt.py

This program is supposed to compute a student's average score and print
whether they passed or failed (passing is 65 or above). But it has THREE
bugs hiding in it!

Type the following code into your new file EXACTLY as written — don't fix
anything yet! Then use PyCharm's features to find and fix each bug.

    scores = [85, 42, 78, 65, 50]
    total = 0

    for score in scores
        total = total + score

    average = total / len(score)

    if average >= 65:
        result = "PASS"
    else:
        result = "PASS"

    print(f"Average: {average}")
    print(f"Result: {result}")

There are three bugs to find — one of each type:

  Bug 1 (Syntax Error): PyCharm will underline something in red before you
      even run the code. Look for the red squiggly line and fix the syntax.

  Bug 2 (Runtime Error): After fixing Bug 1, run the program. It will crash
      with a TypeError. Read the error message in the Run panel — it tells you
      exactly which line has the problem and what went wrong.

  Bug 3 (Logic Error): After fixing Bug 2, the program will run without
      errors — but the output will be WRONG. Compare your output to the
      expected output below and find the line that doesn't do what it should.

Expected correct output:
  Average: 64.0
  Result: FAIL

NOTE: In our next class, we'll learn about PyCharm's built-in debugger — a
tool that lets you pause your program and step through it line by line. That
will make finding bugs like these even easier. This is one of the biggest
advantages of working in a full IDE like PyCharm instead of Colab!
"""


# ==============================================================================
# PROBLEM 6: Batch Data Processing (~15 minutes)
# ==============================================================================
"""
Create a new file called: weather_data.py

A weather station recorded 14 daily high temperatures in Fahrenheit.
Use list comprehensions to analyze the data.

Start with this data:
    temps_f = [45, 52, 48, 61, 55, 37, 42, 58, 63, 50, 47, 59, 64, 53]

Step 1: Convert all temperatures to Celsius using a list comprehension.
    Use the formula from Problem 3: Celsius = (Fahrenheit - 32) * 5/9
    Round each value to 1 decimal place.
    Print the Celsius list.

Step 2: Use a list comprehension with a condition to create a list of only
    the "warm" days — temperatures that are 15°C or above.
    Print the warm days list.

Step 3 (Stretch): Compute the day-to-day temperature changes using a list
    comprehension. Each change is the difference between a day's temperature
    and the previous day's temperature. You will need to use range() and
    indexing inside your comprehension.
    Round each change to 1 decimal place.
    Print the changes list.

    Hint: If your Celsius list is called temps_c, then the change for day i
    is temps_c[i+1] - temps_c[i]. How many changes are there for 14 days?

Expected output:
  Celsius: [7.2, 11.1, 8.9, 16.1, 12.8, 2.8, 5.6, 14.4, 17.2, 10.0, 8.3, 15.0, 17.8, 11.7]
  Warm days: [16.1, 17.2, 15.0, 17.8]
  Changes: [3.9, -2.2, 7.2, -3.3, -10.0, 2.8, 8.8, 2.8, -7.2, -1.7, 6.7, 2.8, -6.1]
"""


# ==============================================================================
# PROBLEM 7: The Collatz Conjecture (~20 minutes) — CHALLENGE
# ==============================================================================
"""
Create a new file called: collatz.py

The Collatz Conjecture is one of the most famous unsolved problems in
mathematics. The rules are simple:
  - Start with any positive integer n.
  - If n is even, divide it by 2.
  - If n is odd, multiply it by 3 and add 1.
  - Repeat until you reach 1.

The conjecture says that no matter what number you start with, you will
ALWAYS eventually reach 1. No one has been able to prove this is true for
every number — but no one has found a counterexample either!

Part A: Write a program that:
  1. Asks the user for a positive integer.
  2. Prints the Collatz sequence starting from that number.
  3. Prints how many steps it took to reach 1.

Example run:
  Enter a positive integer: 6
  6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
  Steps: 8

Hints:
  - Use a while loop that runs as long as n != 1.
  - Use a counter variable for the number of steps.
  - To build the sequence, you could either print as you go (using
    print(n, end=" -> ")) or collect values in a list and join them at
    the end with " -> ".join().
  - To check if a number is even, use: n % 2 == 0

CHALLENGE (Part B): After Part A works, find which starting number between
1 and 100 produces the LONGEST Collatz sequence. Print that number and how
many steps it takes. (No user input needed for this part — just loop
through all 100 starting numbers.)
"""
