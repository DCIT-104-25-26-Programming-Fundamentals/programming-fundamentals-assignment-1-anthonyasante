# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    """
    Calculates the sum of all elements in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """
    Calculates the average of the elements in the list.
    """
    if not numbers:
        return 0
    
    total = calculate_sum(numbers)
    return total / len(numbers)

def find_maximum(numbers):
    """
    Finds the maximum value in the list without using max().
    """
    if not numbers:
        return None
        
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def find_minimum(numbers):
    """
    Finds the minimum value in the list without using min().
    """
    if not numbers:
        return None
        
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def main():
    """
    Handles user input, populates the list, and prints statistical results.
    """
    try:
        n_input = input("How many numbers? ")
        n = int(n_input)
        
        if n <= 0:
            print("Error: The number of items must be a positive integer.")
            return
            
        numbers = []
        for i in range(1, n + 1):
            val = float(input(f"Enter number {i}: "))
            # Convert to int if it's a whole number for cleaner output matching the example
            if val.is_integer():
                val = int(val)
            numbers.append(val)
            
        # Calculate statistics
        total = calculate_sum(numbers)
        average = calculate_average(numbers)
        maximum = find_maximum(numbers)
        minimum = find_minimum(numbers)
        
        # Display results
        print("\nResults:")
        print(f"Sum:     {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
        
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()