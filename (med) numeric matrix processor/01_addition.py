# create matrix from user input
def get_matrix(size):
    matrix = []
    for x in range(size[0]):
        row = input().split()
        for y in range(size[1]):
            row[y] = int(row[y])
        matrix.append(row)
    return matrix


# add two matrices together
def add_matrix(matrixA, matrixB, size):
    matrix = []
    for x in range(size[0]):
        for y in range(size[1]):
            matrix[x][y] = matrixA[x][y] + matrixB[x][y]
    return matrix


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=' ')
        print()


# main code
a_size = [int(a) for a in input().split()]
a_matrix = get_matrix(a_size)
b_size = [int(b) for b in input().split()]
b_matrix = get_matrix(b_size)
if a_size[0] != b_size[0] or a_size[0] != b_size[0]:
    print('ERROR')
else:
    sum_matrix = [[a_matrix[x][y] + b_matrix[x][y] for y in range(a_size[1])] for x in range(a_size[0])]
    print_matrix(sum_matrix)
