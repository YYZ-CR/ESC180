import copy
def lowercase(s):
    return s.lower()

def g(L):
    for i in range(len(L)):
        L[i] += 1
    return L

def g1(L):
    ll = []
    for i in range(len(L)):
        ll.append(L[i] + 1)
    return ll

def binary_search(L, e):
    low = 0
    high = len(L)-1
    iterations = 1
    while high-low >= 2:
        iterations += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid, iterations
    if L[low] == e:
        return low, iterations
    elif L[high] == e:
        return high, iterations
    else:
        return None, iterations

def main():
    s = input()
    s = lowercase(s)
    print(s)
    print('====================') #q1 b
    l = [1,2,3]
    print(l)
    print(id(l))
    g(l)
    print(l)
    print(id(l))
    l = g1(l)
    print(l)
    print(id(l))
    print('====================')#q1 c&d
    d = {'a': [1,2], 'b': 2}
    c = d.copy()
    print(c)
    print(id(c))
    print(d)
    print(id(d))
    c['a'][1]= 3
    print(c)
    print(d)
    print('====================')#q1 e
    d = {'a': [1,2], 'b': 2}
    c = copy.deepcopy(d)
    print(c)
    print(id(c))
    print(d)
    print(id(d))
    c['a'][1] = 3
    print(c)
    print(d)
    print('====================')#q2
    b,iterations = binary_search([1,2,3,4,5,6,7,8,9,10], 3)
    print(b, iterations)
    import time
    print('====================')#q2e
    for j in (10,100,1000,100000):
        listt = []
        for i in range(j):
            listt.append(i)
        start = time.time()
        print(binary_search(listt, i)[1])   
        end = time.time()
        print(end-start)
    
    start = time.time()
    for i in range(100000):
        if listt[i] == 99999:
            break
    end = time.time()
    print(end-start)

    



if __name__ == '__main__':
    main()
