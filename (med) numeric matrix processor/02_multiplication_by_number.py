# create matrix from user input
def get_matrix(size):
    matrix = []
    for x in range(size[0]):
        row = input().split()
        for y in range(size[1]):
            row[y] = int(row[y])
        matrix.append(row)
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
multiplier = int(input())
prod_matrix = [[a_matrix[x][y] * multiplier for y in range(a_size[1])] for x in range(a_size[0])]
print_matrix(prod_matrix)
