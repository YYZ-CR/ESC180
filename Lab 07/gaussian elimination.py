import numpy as np
import time

def print_matrix(M_lol):
    print('The matrix is currently:')
    print(np.array(M_lol))

def get_lead_ind(row): # index of first non-zero number
    index = 0
    for i in range(len(row)):
        if row[i] != 0:
            break
        index+=1
    '''if index == len(row):
        return 0'''
    return index

def get_row_to_swap(M, start_i): # finds a row that needs to be swapped with the start_i row for gaussian elimination
    swap_row = -1
    for i in range(len(M[1])):
        for j in range (start_i, len(M)):
            if i == get_lead_ind(M[j]):
                swap_row = j
                break
        if swap_row != -1:
            break
    return swap_row

def add_rows_coefs(r1, c1, r2, c2): # adds two rows
    new_list = []
    for i in range(len(r1)):
        new_list.append(c1*r1[i]+c2*r2[i])
    return new_list

def eliminate(M:list, row_to_sub:int, best_lead_ind:int): # eliminates all entries below a certain row in the same column
    ind = get_lead_ind(M[row_to_sub])
    for i in range(best_lead_ind, len(M)):
        if ind >= len(M[0]):
            break
        if M[i][ind] != 0:
            M[i] = add_rows_coefs(M[i],M[row_to_sub][ind],M[row_to_sub],-M[i][ind])

def forward_step(M):
    print_matrix(M)
    for i in range(len(M)):
        print(f'Now looking at row {i}')
        swap_row = get_row_to_swap(M,i)
        swap_column = get_lead_ind(M[swap_row])
        if swap_column < len(M[i]):
            print(f'Swapping rows {i} and {swap_row} so that entry {swap_column} in the current row is non-zero')
            M[i], M[swap_row] = M[swap_row], M[i]               
        print_matrix(M)
        print(f'Adding row {i} to rows below it to eliminate coefficients in column {swap_column}')
        eliminate(M, i, i+1)
        print_matrix(M)
        print('================================================================================')
    print('Done with this forward step')
    print_matrix(M)

def backward_step(M):
    for i in range(len(M)-1,-1,-1):
        print(f'Adding row {i} to rows above it to eliminate coefficients in column {get_lead_ind(M[i])}')
        M[i], M[0] = M[0], M[i]
        eliminate(M,0,1)
        M[i], M[0] = M[0], M[i]
        print_matrix(M)
        print('================================================================================')
    print('Now dividing by each row by the leading coefficient')
    for i in range(len(M)):
        for j in range(len(M[i])-1,-1,-1):
            if M[i][j] not in [0,1]:
                M[i][j] = round(M[i][j] / M[i][get_lead_ind(M[i])])
    print_matrix(M)
    print('================================================================================')

def solve(M, b):
    if len(M) != len(b):
        return 0
    augmented_matrix = M
    for i in range(len(b)):
        augmented_matrix[i].append(b[i])
    forward_step(augmented_matrix)
    backward_step(augmented_matrix)
    solution = []
    for i in range(len(augmented_matrix)):
        solution.append(augmented_matrix[i][-1])
    print('The solution is:')
    print(np.array(solution))
    return solution


if __name__ == '__main__':
    matrix =  [[ 0, 0, 1, 0, 2,],
               [ 1, 0, 2, 3, 4,],
               [ 3, 0, 4, 2, 1,],
               [ 1, 0, 1, 1, 2,]]
    
    forward_step(matrix)

    matrix =  [[ 1,-2, 3, 22],
 [ 3, 10, 1, 314],
 [ 1, 5, 3, 92]]
    
    forward_step(matrix)
    backward_step(matrix)

    matrix = [[ 1,-2, 3],
 [ 3, 10, 1],
 [ 1, 5, 3]]
    b = [22, 314, 92]
    solve(matrix, b)

    #testing random matrices

    matrix = [[1,-2,3],[3,10,1],[1,5,3]]
    x = np.array([75,10,-11])
    b = np.matmul(np.array(matrix),x).tolist()

    if solve(matrix,b) == [75,10,-11]:
        print('q1 correct')
    time.sleep(2)

    matrix = [[1,1,1],[2,-1,1],[1,-1,2]]
    x = np.array([1,2,2])
    b = np.matmul(np.array(matrix),x).tolist()

    if solve(matrix,b) == x.tolist():
        print('q2 correct')
    time.sleep(2)

    matrix = [[2,3,1],[1,-1,2],[4,1,-1]]
    x = np.array([10,5,1])
    b = np.matmul(np.array(matrix),x).tolist()

    if solve(matrix,b) == [10,5,1]:
        print('q3 correct')
