# create matrix from user input
def get_matrix(size):
    matrix = []
    for x in range(size[0]):
        row = input().split()
        for y in range(size[1]):
            row[y] = float(row[y])
        matrix.append(row)
    return matrix


# multiply matrix by constant
def mult_const():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    multiplier = float(input('Enter constant: '))
    prod_matrix = [[matrix[x][y] * multiplier for y in range(size[1])] for x in range(size[0])]
    print('The result is:')
    print_matrix(prod_matrix)


# multiply two matrices together
def mult_matrices():
    a_size = [int(a) for a in input('Enter size of first matrix: ').split()]
    print('Enter first matrix:')
    a_matrix = get_matrix(a_size)
    b_size = [int(b) for b in input('Enter size of second matrix: ').split()]
    print('Enter second matrix:')
    b_matrix = get_matrix(b_size)
    prod_matrix = [[sum(a*b for a,b in zip(a_row,b_col)) for b_col in zip(*b_matrix)] for a_row in a_matrix]
    print_matrix(prod_matrix)


# add two matrices together
def add_matrices():
    a_size = [int(a) for a in input('Enter size of first matrix: ').split()]
    print('Enter first matrix:')
    a_matrix = get_matrix(a_size)
    b_size = [int(b) for b in input('Enter size of second matrix: ').split()]
    print('Enter second matrix:')
    b_matrix = get_matrix(b_size)
    if a_size[0] != b_size[0] or a_size[0] != b_size[0]:
        print('ERROR')
    else:
        sum_matrix = [[a_matrix[x][y] + b_matrix[x][y] for y in range(a_size[1])] for x in range(a_size[0])]
        print_matrix(sum_matrix)


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(*row)


# main code
while True:
    print(r'''1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        0. Exit''')
    choice = int(input('Your choice: '))
    if choice == 0:
        exit()
    elif choice == 1:
        add_matrices()
    elif choice == 2:
        mult_const()
    elif choice == 3:
        mult_matrices()
