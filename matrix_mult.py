#project-9b

#Gabriel Venegas
#GitHub username: GVenegas1
#Date: 11/26/2025


# This function does the dot product of two lists.
# Dot product = multiply the numbers in the same spots and add them.
def dot_prod(a, b):

    # If the lists are not the same size, we can't do it.
    if len(a) != len(b):
        return None

    total = 0

    # Go through each position in the lists
    for i in range(len(a)):
        # multiply the two numbers and add to total
        total = total + (a[i] * b[i])

    return total



# This function multiplies 2 matrices
def matrix_mult(A, B):

    # A columns = len(A[0])
    # B rows = len(B)
    # If these don't match then matrix multiply does not work
    if len(A[0]) != len(B):
        return None

    result = []  # this will be the final matrix

    # Loop through each row of A
    for row in A:

        new_row = []  # this will store one full row of the answer

        # Loop through each column number in B
        for col_num in range(len(B[0])):

            # Make the column from B
            col = []
            for r in range(len(B)):
                col.append(B[r][col_num])

            # Now do the dot product of (row from A) and (column from B)
            value = dot_prod(row, col)

            # Add this answer to the row we are building
            new_row.append(value)

        # Now add this whole row to the result matrix
        result.append(new_row)

    return result



# Testing here
if __name__ == "main":
    A = [[3, 1], [-8, 5], [1, 4]]
    B = [[1, 4, 7, 1], [-5, -8, 4, 3]]
    print(matrix_mult(A, B))
