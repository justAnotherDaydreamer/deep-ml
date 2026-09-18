def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # Let original matrix be A_ij
    # Make the matrix b:
    b = []

    for j in range(len(a[0])):  # For each column in a (valid input no empty):
        temp = []  # Will be added to b
        for i in range(len(a)):  # For each row in that column:
            # Swap row i column j to row j column i
            temp.append(a[i][j])
            
        b.append(temp)
    
    return b