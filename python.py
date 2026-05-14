
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Create empty matrix with swapped dimensions
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

# Example Execution
matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix))
# Output: [[1, 4], [2, 5], [3, 6]]
def transpose_matrix_copilot(matrix):
    # zip(*matrix) unpacks rows and groups matching column items
    return [list(row) for row in zip(*matrix)]

# Example Execution
matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix_copilot(matrix))
# Output: [[1, 4], [2, 5], [3, 6]]
