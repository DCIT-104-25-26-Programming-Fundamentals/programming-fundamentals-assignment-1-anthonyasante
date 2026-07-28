# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_fibonacci_terms(n):
    """
    Generates and prints the first N terms of the Fibonacci sequence.
    """
    if n <= 0:
        print("Error: The number of terms must be a positive integer.")
        return
        
    if n == 1:
        print("Fibonacci sequence: 0")
        return
        
    # Start the sequence with the first two numbers
    a, b = 0, 1
    sequence = [a, b]
    
    # Generate the remaining n-2 terms using a loop
    for _ in range(n - 2):
        next_val = a + b
        sequence.append(next_val)
        # Update a and b for the next iteration
        a = b
        b = next_val
        
    # Format and print the sequence on one line
    str_sequence = [str(x) for x in sequence]
    print(f"Fibonacci sequence: {' '.join(str_sequence)}")


def is_fibonacci_number(num):
    """
    Checks if a given number belongs to the Fibonacci sequence using a loop.
    Returns True if it is, False otherwise.
    """
    if num < 0:
        return False
        
    if num == 0 or num == 1:
        return True
        
    a, b = 0, 1
    # Generate Fibonacci numbers until we match or exceed the target number
    while b < num:
        next_val = a + b
        a = b
        b = next_val
        
    # If the current number matches the target, it's a Fibonacci number
    return b == num


def main():
    """
    Handles user input and coordinates the program logic for Parts A and B.
    """
    try:
        # --- PART A ---
        n_input = input("How many terms? ")
        n = int(n_input)
        
        # Check for positive integer logic before calling to prevent printing Part B blindly on error
        if n <= 0:
             print("Error: The number of terms must be a positive integer.")
        else:
             print_fibonacci_terms(n)
        
        print() # Adding a newline for readability between parts
        
        # --- PART B ---
        num_input = input("Enter a number to check: ")
        num = int(num_input)
        
        if is_fibonacci_number(num):
            print(f"{num} is a Fibonacci number.")
        else:
            print(f"{num} is NOT a Fibonacci number.")
            
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()