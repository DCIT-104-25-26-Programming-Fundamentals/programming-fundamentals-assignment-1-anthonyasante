# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_single_table(num):
    """
    Prints the multiplication table for a given number from 1 to 12.
    """
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        # Using format specifiers to align the output neatly
        print(f"{num} x {i:2} = {num * i}")

def print_multiple_tables(n):
    """
    Prints the full multiplication table for every number from 1 to N,
    separated by dashed lines.
    """
    for i in range(1, n + 1):
        print_single_table(i)
        # Print a separator after each table except the last one
        if i < n:
            print("-" * 27)

def main():
    """
    Handles user input and executes the logic for Parts A and B.
    """
    try:
        # --- PART A ---
        print("--- PART A: Single Table ---")
        num_input = input("Enter a number: ")
        num = int(num_input)
        print()
        print_single_table(num)
        
        print() # Add spacing between parts
        
        # --- PART B ---
        print("--- PART B: Tables from 1 to N ---")
        n_input = input("Enter a number N: ")
        n = int(n_input)
        
        # Validate that N is a positive integer
        if n <= 0:
            print("Error: The number must be a positive integer.")
        else:
            print()
            print_multiple_tables(n)
            
    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()