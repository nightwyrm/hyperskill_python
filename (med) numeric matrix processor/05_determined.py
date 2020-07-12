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


# transpose a matrix along the main diagonal
def main_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    new_matrix = map(list, zip(*matrix))
    print('The result is:')
    print_matrix(new_matrix)


# transpose a matrix along the side diagonal
def side_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    for row in matrix:
        row = row.reverse()
    matrix = matrix[::-1]
    new_matrix = map(list, zip(*matrix))
    print('The result is:')
    print_matrix(new_matrix)


# transpose a matrix along the vertical axis
def vert_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    for row in matrix:
        row = row.reverse()
    print('The result is:')
    print_matrix(matrix)


# transpose a matrix along the horizontal axis
def hori_trans():
    size = [int(a) for a in input('Enter size of matrix: ').split()]
    print('Enter matrix:')
    matrix = get_matrix(size)
    matrix = matrix[::-1]
    print('The result is:')
    print_matrix(matrix)


# calculate the determinant for a matrix
def calc_det(matrix, total=0):
    indices = list(range(len(matrix)))
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val
    for focus in indices:
        submatrix = [row[:] for row in matrix]
        submatrix = submatrix[1:]
        height = len(submatrix)
        for i in range(height):
            submatrix[i] = submatrix[i][0:focus] + submatrix[i][focus+1:]
        sign = (-1) ** (focus % 2)
        sub_det = calc_det(submatrix)
        total += sign * matrix[0][focus] * sub_det
    return total


# print a matrix
def print_matrix(matrix):
    for row in matrix:
        print(*row)


# main code
while True:
    print(r'''1. Add matrices
        2. Multiply matrix by a constant
        3. Multiply matrices
        4. Transpose matrix
        5. Calculate a determinant
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
    elif choice == 4:
        print(r'''1. Main diagonal
            2. Side diagonal
            3. Vertical line
            4. Horizontal line''')
        tr_choice = int(input('Your choice: '))
        if tr_choice == 1:
            main_trans()
        elif tr_choice == 2:
            side_trans()
        elif tr_choice == 3:
            vert_trans()
        elif tr_choice == 4:
            hori_trans()
    elif choice == 5:
            det_size = [int(a) for a in input('Enter size of matrix: ').split()]
            print('Enter matrix:')
            det_matrix = get_matrix(det_size)
            determ = calc_det(det_matrix)
            print('The result is:')
            print(str(determ))
