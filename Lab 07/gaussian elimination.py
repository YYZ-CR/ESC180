import numpy as np


def print_matrix(M_lol):
    print(np.array(M_lol))

def get_lead_ind(row): # index of first non-zero number
    index = 0
    for i in range(len(row)):
        if row[i] != 0:
            index+=1
    return index

def get_row_to_swap(M, start_i): # finds a row that needs to be swapped with the start_i row for gaussian elimination
    swap_row = -1
    for i in range(len(M)):
        for j in range (start_i, len(M)):
            if i == get_lead_ind(M[j]):
                swap_row = j
        if swap_row != -1:
            break
    return swap_row

def add_rows_coefs(r1, c1, r2, c2): # adds two rows
    new_list = []
    for i in range(len(r1)):
        new_list.append(c1*r1[i]+c2*r2[i])
    return new_list

def eliminate(M, row_to_sub, best_lead_ind): # eliminates all entries below a certain row in the same column
    ind = get_lead_ind(M[row_to_sub])
    for i in range(best_lead_ind, len(M)):
        if M[i][ind] > 0:
            for j in range(len(M[i])):
                M[i][j] -= M[row_to_sub][j]*(M[i][ind]/M[row_to_sub][ind])
        elif M[i][ind] < 0:
            for j in range(len(M[i])):
                M[i][j] += M[row_to_sub][j]*(M[i][ind]/M[row_to_sub][ind])

def forward_step(M):
    print('The matrix is currently:')
    print_matrix(M)
    for i in range(len(M)):
        





if __name__ == '__main__':
    