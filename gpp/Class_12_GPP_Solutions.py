"""
================================================================================
EK125 — Week 7A Morning Assignment: Python Dictionaries
Group Exercise (Teams of 3)

** INSTRUCTOR SOLUTIONS — DO NOT DISTRIBUTE TO STUDENTS **
================================================================================
"""

# ==============================================================================
# Problem 1: Dictionary basics
# ==============================================================================

# --- 1.1: Make a dictionary ---
hurricane = {'name': 'Sandy', 'year': 2012, 'category': 3}
print(hurricane['year'])       # Output: 2012


# --- 1.2: Add new key-value pairs ---
hurricane['pressure'] = 940    # add new key
hurricane['category'] = 4      # update existing key
print(hurricane)
# Output: {'name': 'Sandy', 'year': 2012, 'category': 4, 'pressure': 940}


# --- 1.3: Loop over key-value pairs ---
for key, value in hurricane.items():
    print(f"{key}: {value}")
# Output:
#   name: Sandy
#   year: 2012
#   category: 4
#   pressure: 940


# ==============================================================================
# Problem 2: Book information
# ==============================================================================

# Step 1: Create the dictionary
book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year_published': 1960,
    'genre': 'Fiction'
}

# Step 2: Print the value for 'author'
print("Author:", book['author'])             # Output: Harper Lee

# Step 3: Check if 'pages' exists
has_pages = 'pages' in book
print("Does the 'pages' key exist?", has_pages)   # Output: False

# Step 4: Number of key-value pairs
num_pairs = len(book)
print("Number of key-value pairs:", num_pairs)     # Output: 4


# ==============================================================================
# Problem 3: get() and pop() on a smartphone dictionary
# ==============================================================================

# Define the dictionary
smartphone = {
    'brand': 'Apple',
    'model': 'iPhone 13',
    'year_released': 2021,
    'price': 799
}

# Step 1: Retrieve price using get()
price = smartphone.get('price')
print("Price:", price)                        # Output: 799

# Step 2: Add storage key
smartphone['storage'] = '128GB'

# Step 3: Update price
smartphone['price'] = 749

# Step 4: Remove 'year_released' using pop()
smartphone.pop('year_released')

# Step 5: Print updated dictionary
print("\nUpdated Dictionary:", smartphone)
# Output: {'brand': 'Apple', 'model': 'iPhone 13', 'price': 749, 'storage': '128GB'}


# ==============================================================================
# Problem 4: clear() on a shopping cart dictionary
# ==============================================================================

shopping_cart = {
    'apple': 4,
    'banana': 6,
    'milk': 2,
    'bread': 1
}

# Step 1: Print current contents
print("Shopping Cart Contents:", shopping_cart)
# Output: {'apple': 4, 'banana': 6, 'milk': 2, 'bread': 1}

# Step 2: Clear the cart
shopping_cart.clear()

# Step 3: Confirm it is empty
print("Shopping Cart after clear():", shopping_cart)   # Output: {}


# ==============================================================================
# Problem 5: .keys(), .values() and .items()
# ==============================================================================

store_stock = {
    'apples': 50,
    'bananas': 30,
    'milk': 20,
    'bread': 15
}

# Step 1: .keys() — list all items
items = list(store_stock.keys())
print("\nItems in store:", items)

# Step 2: .values() — total stock
total_stock = sum(store_stock.values())
print("\nTotal stock:", total_stock)           # Output: 115

# Step 3: .items() — print as tuples
print("\nItem-stock tuples:")
for item_tuple in store_stock.items():
    print(item_tuple)

# Step 4: loop with formatted output
print("Stock details:")
for item, stock in store_stock.items():
    print(f"Item: {item}, Stock: {stock}")


# ==============================================================================
# Problem 6: Challenge — nested dictionaries
# ==============================================================================

students_scores = {
    'Alice':   {'Math': 85, 'Science': 90, 'English': 88},
    'Bob':     {'Math': 78, 'Science': 82, 'English': 84},
    'Charlie': {'Math': 92, 'Science': 88, 'English': 91},
    'Dana':    {'Math': 89, 'Science': 94, 'English': 87}
}

# Step 1: Print Alice's scores
print("Alice's Scores:", students_scores['Alice'])

# Step 2: Charlie's Science score
charlie_science = students_scores['Charlie']['Science']
print("\nCharlie's Science Score:", charlie_science)   # Output: 88

# Step 3: Add new student Eve
students_scores['Eve'] = {'Math': 88, 'Science': 86, 'English': 89}

# Step 4: Average Math score across all students
math_scores = [scores['Math'] for scores in students_scores.values()]
average_math_score = sum(math_scores) / len(math_scores)
print("\nAverage Math Score:", average_math_score)     # Output: 86.4

# Step 5: Each student's average score
print("\nStudent Average Scores:")
for student, scores in students_scores.items():
    average_score = sum(scores.values()) / len(scores)
    print(f"Student: {student}, Average Score: {average_score:.2f}")
# Output:
#   Student: Alice,   Average Score: 87.67
#   Student: Bob,     Average Score: 81.33
#   Student: Charlie, Average Score: 90.33
#   Student: Dana,    Average Score: 90.00
#   Student: Eve,     Average Score: 87.67
