def my_sqrt(x):
    sqr = x**.5
    return sqr

def my_print_square(x):
    sqr = my_sqrt(x)
    print(sqr)

if __name__ == "__main__":
    res = my_sqrt(25)
    print(res)
    print(my_print_square(25))
    # won't work because sqr is a local variable inside the function my_sqrt
    # you can modify print(sqr) to print(res) so it doesn't produce an error
    my_print_square(25)
    # the difference between calling my_sqrt and my_print_square is that my_sqrt returns the square root of the number
    # but my_print_square prints the square root of the number

    # the output for the following code should be a 0 becasue the function my_print_square doesn't return anything
    res = my_print_square(25)
    print(res)
    
    

