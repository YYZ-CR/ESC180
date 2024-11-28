# problem 1
# part a & b

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# part c
# call tree for power(2, 3)
'''
power(2, 0)
            | 
            1
            |
power(2, 1)
            |
            2 * 1
            |
power(2, 2)
            |
            2 * 2 * 1
            |
power(2, 3)
            | 2 * 2 * 2 * 1
'''


# problem 2
def sum_digits(number):
    if len(str(number)) == 0:
        return 0
    else:
        return int(str(number)[0]) + sum_digits(str(number)[1:])
    

def main():
    print(sum_digits(123454321))

if __name__ == '__main__':
    main()