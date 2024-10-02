from math import pi
global pi_approx

def formula(n):
    return ((-1)**n)/(2*n+1)*4

def n_sig_figs(n):
    pi_approx = 0
    m = 0
    while (int(pi * 10**(n-1)) - int(pi_approx * 10**(n-1))) != 0: # could also use abs()
        pi_approx += formula(m)
        m += 1
    return m

if __name__ == '__main__':
    # question 1
    pi_approx = 0
    n = 1000
    for i in range (n,-1,-1):
        pi_approx += formula(i)

    print(pi_approx)

    # question 2
    pi_approx = 0
    n = 1000
    while n >= 0:
        pi_approx += formula(n)
        n -= 1
    print(pi_approx)

    # question 6
    print(n_sig_figs(0))