def get_nums(L): #problem 2
    nums = []
    for i in L:
        if type(i) == int:
            nums.append(i)
    return nums

def look_up(L, num): #problem 3
    for i in L:
        if num == i[1]:
            return i[0]
    return None

def E(x0, x1, x2, w01, w02, w12): #problem 4
    term1 = x0 * x1 * w01
    term2 = x0 * x2 * w02
    term3 = x1 * x2 * w12
    return -(term1 + term2 + term3)

def opt_weight(x0, x1, x2, w01, w02, w12):
    if x0*x1>0:
        w01 += 0.1
    else:
        w01 -= 0.1
    if x0*x2>0:
        w02 += 0.1
    else:
        w02 -= 0.1
    if x1*x2>0:
        w12 += 0.1
    else:
        w12 -= 0.1
    return w01, w02, w12

def print_all_energies(w01, w02, w12):
    for x0 in [-1, 1]:
        for x1 in [-1, 1]:
            for x2 in [-1, 1]:
                print("x: (", x0, x1, x2, ")", "E:", E(x0, x1, x2, w01, w02, w12))

def repeat(x0,x1,x2,w01,w02,w12,num):
    for i in range(num):
        w01,w02,w12 = opt_weight(x0, x1, x2, w01, w02, w12)
    return w01, w02, w12
    

if __name__ == '__main__':     
    #problem 1
    L = [["CIV", 92],
    ["180", 98],
    ["103", 99],
    ["194", 95]]

    for i in L:
        if i[1] == 99:
            print(i[0])     
        
    #problem 2
    print(get_nums(L))

    #problem 3
    print(look_up(L, 99))

    #problem 4
    w01 = 2
    w02 = -1
    w12 = 1
    print_all_energies(w01, w02, w12)
    #part b
    x0 = 1
    x1 = -1
    x2 = -1
    print('======================')
    w01, w02, w12 = opt_weight(x0, x1, x2, w01, w02, w12)
    print_all_energies(w01, w02, w12)
    #part c
    w01,w02,w12 = repeat(x0,x1,x2,w01,w02,w12,4)
    print('======================')
    print_all_energies(w01, w02, w12)