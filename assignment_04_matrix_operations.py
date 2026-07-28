# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def transpose_matrix(matrix):
    """
    Computes and returns the transpose of an M x N matrix.
    Result will be an N x M matrix.
    """
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an N x M matrix with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Populate the transposed matrix using nested loops
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed

def add_matrices(matrix1, matrix2):
    """
    Computes and returns the element-wise sum of two M x N matrices.
    """
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Add corresponding elements using nested loops
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    return result

def multiply_matrices(matrix_a, matrix_b):
    """
    Computes and returns the matrix product of Matrix A (M x N) and Matrix B (N x P).
    Result will be an M x P matrix.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    # rows_b is the same as cols_a
    cols_b = len(matrix_b[0])
    
    # Initialize an M x P result matrix with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Multiply matrices using three nested loops
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result

def read_matrix(rows, cols, matrix_name="Matrix"):
    """
    Helper function to read a matrix from user input row by row.
    """
    matrix = []
    print(f"\nEntering values for {matrix_name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}: ")
                
                # Split the input string and convert to numbers (int if whole, else float)
                row_values = []
                for x in row_input.split():
                    val = float(x)
                    if val.is_integer():
                        val = int(val)
                    row_values.append(val)
                
                if len(row_values) != cols:
                    print(f"Error: Expected {cols} values separated by spaces, but got {len(row_values)}.")
                    continue
                    
                matrix.append(row_values)
                break
                
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
                
    return matrix

def print_matrix(matrix, title):
    """
    Helper function to print a matrix in an aligned grid format.
    """
    print(f"\n{title}:")
    if not matrix:
        print("Empty Matrix")
        return
        
    for row in matrix:
        # Formats each value to be right-aligned with a width of 5 characters
        formatted_row = " ".join(f"{val:>5}" for val in row)
        print(formatted_row)

def main():
    try:
        print("==================================================")
        print(" PART A — Transpose a Matrix")
        print("==================================================")
        rows_a = int(input("Enter number of rows: "))
        cols_a = int(input("Enter number of columns: "))
        matrix_a = read_matrix(rows_a, cols_a, "Original Matrix")
        
        print_matrix(matrix_a, "Original Matrix")
        transposed = transpose_matrix(matrix_a)
        print_matrix(transposed, "Transposed Matrix")
        
        print("\n==================================================")
        print(" PART B — Add Two Matrices")
        print("==================================================")
        print("Note: Matrices must be exactly the same size.")
        rows_b = int(input("Enter number of rows: "))
        cols_b = int(input("Enter number of columns: "))
        
        m1 = read_matrix(rows_b, cols_b, "Matrix 1")
        m2 = read_matrix(rows_b, cols_b, "Matrix 2")
        
        sum_matrix = add_matrices(m1, m2)
        print_matrix(sum_matrix, "Sum of Matrix 1 and Matrix 2")
        
        print("\n==================================================")
        print(" PART C — Multiply Two Matrices")
        print("==================================================")
        print("Note: The number of columns in A must equal the number of rows in B.")
        m_rows = int(input("Enter number of rows for Matrix A (M): "))
        m_cols = int(input("Enter number of columns for Matrix A / rows for Matrix B (N): "))
        p_cols = int(input("Enter number of columns for Matrix B (P): "))
        
        mat_a = read_matrix(m_rows, m_cols, "Matrix A")
        mat_b = read_matrix(m_cols, p_cols, "Matrix B")
        
        product_matrix = multiply_matrices(mat_a, mat_b)
        print_matrix(product_matrix, "Product Matrix (A × B)")
        
    except ValueError:
        print("\nError: Please enter valid integers for matrix dimensions.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()