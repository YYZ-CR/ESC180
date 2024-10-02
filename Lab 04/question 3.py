# question 3
def gcd_one(n,m):
    gcd = 1
    for i in range(1,min(n,m)+1):
        if n%i == 0 and m%i == 0:
            gcd = i
    return gcd

def gcd_two(n, m):
    number = min(n, m)
    while number > 0:
        if n % number == 0 and m % number == 0:
            return number
        number -= 1

# question 4
def simplify_fraction(n,m):
    gcd = gcd_two(n,m)
    n //= gcd
    m //= gcd
    if m == 1:
        print(n)
    else:
        print(f'{n}/{m}')

# question 8
def euclidean(n,m):
    big = max(n,m)
    small = min(n,m)
    while(big%small != 0):
        big, small = small, big%small
    return small

if __name__ == "__main__":
    # question 3
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))
    print(gcd_one(n, m))
    print(gcd_two(n, m))
    # question 4
    simplify_fraction(n, m)
    # question 8
    print(f'{euclidean(n,m)}')


