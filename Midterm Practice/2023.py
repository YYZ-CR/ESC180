def print_halloween(month, day):
    if month == 'oct' and day == 31:
        print('Happy Haloween')
    else:
        print('Not Haloween')

def sum_even_squares(L):
    sum = 0
    for i in L:
        if i%2 == 0:
            sum+= i*i
    return sum

def is_sorted(L):
    for i in range(1,len(L)):
        if L[0] < L[1] and L[i] > L[i-1]: #increasing
            pass
        elif L[0] > L[1] and L[i] < L[i-1]: #decreasing
            pass
        else:
            break
        if i == len(L)-1:
            return True
    return False

def print_trick_or_treat_for(name):
    if name in ['cluett', 'stangeby']:
        print('trick')
    elif name == 'davis':
        print('treat')
    else:
        print('no candy for you')

def count_occurences(L,n):
    count = 0
    for i in L: 
        if i == n:
            count+=1
    return count

def most_frequent_fave(faves):
    candy_list = {}
    for i in faves:
        if i in candy_list.keys():
            candy_list[i] += 1
        else:
            candy_list[i] = 1
    return list(candy_list.keys())[list(candy_list.values()).index(max(candy_list.values()))]

next_prime = 2

def check_next_prime(n):
    global next_prime
    if next_prime == 0:
        print('Game is over')
    elif n == next_prime:
        print('Correct')
        test_prime = next_prime+1
        while True: #finds next prime number
            for i in range(2, (test_prime+1)//2+1):
                if test_prime % i == 0:
                    break
                elif i >= (test_prime+1)//2-1:
                    next_prime = test_prime
            if test_prime == next_prime:
                break
            else:
                test_prime +=1
    else:
        print('Incorrect, game over')
        next_prime = 0

def is_almost_symmetric(M):
    if len(M) == len(M[0]):
        count = 0
        not_diag = []
        for r in range(len(M)):
            for c in range (len(M)):
                if c != r:
                    not_diag.append(M[r][c])
        for r in range(len(M)):
            for c in range(r,len(M)):
                if M[r][c] == M[c][r]:
                    if M[c][c] == M[c][r]:
                        if not_diag.count(M[c][r]) % 2 == 1:
                            count+=1
                else:
                    count+=1
        if count == 2: #this is true if it's possible to switch 2 values and for the matrix to be symmetric
            return True
    return False

from math import pi
def bonus(): #idk if this works
    PI = pi
    denominators = []
    for j in range(100000):
        denominators.append(2*j+1)
    denominator = denominators[0]
    for i in range(1,len(denominators)):
        denominator *= denominators[i]
    numerator = 0
    for i in range(len(denominators)):
        numerator += denominator//denominators[i]*(-1)**i
    pi_est = int(4*(10**1000)*numerator//denominator)
    for i in range(len(str(pi_est))):
        print(str(pi_est)[i],end='')
                    
def main():
    faves = ['candy', 'costumes', 'midterms', 'candy']
    print(most_frequent_fave(faves))
    check_next_prime(2)
    check_next_prime(3)
    check_next_prime(4)
    check_next_prime(5)
    m = [[1,2,4],[2,5,9],[4,3,3]]
    print(is_almost_symmetric(m))
    print()
    bonus()

if __name__ == '__main__':
    main()