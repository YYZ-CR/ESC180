import random

#problem 1
def count_evens(L):
    count = 0
    for i in L:
        if i % 2 == 0:
            count += 1
    return count

#problem 2
def list_to_string(lis:list):
    s = "[" + str(lis[0])
    if len(lis) > 1:
        for i in range (1, len(lis)):
            s += ', ' + str(lis[i])
    s += ']'
    return s

#problem 3
def lists_are_the_same(list1:list, list2:list):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

#probelm 4
def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

#problem 5
def match_pattern(list1, list2):
    for i in range (len(list1)-len(list2)):
        if list1[i] == list2[0]:
            for j in range(len(list2)):
                if list1[i+j] == list2[j]:
                    if j == len(list2)-1:
                        return True
                else:
                    break
    return False

#problem 6
def duplicates(list0):
    for i in range(1,len(list0)):
        if list0[i]==list0[i-1]:
            return True
    return False

#problem 7
def slope(dx, dt):
    return round(dx/dt,2)

def inst_velo(x:list, time:float):
    if time > 0.2 and time < len(x)/10: #if not at extremes
        return (slope(x[int(time*10)+1]-x[int(time*10)-1], 0.2)+ slope(x[int(time*10)+2]-x[int(time*10)-2], 0.4))/2
    elif time < 0.2: #if near min time
        if int(time*10) == 0:
            return slope(x[1]-x[0], 0.1)
        return slope(x[2]-x[0], 0.2)
    else: #if near max time
        if int(time*10) == len(x):
            return slope(x[-1]-x[-2], 0.1)
        return slope(x[-1]-x[-3], 0.2)


if __name__ == '__main__':
    n = [1,2,3]
    m = [1,2,2]
    p = [1,2,3,4]
    o = [1,2,3]
    q = [2,3,4]
    x = [1,2,3,4,5,6,7,8,9,10]
    # q1
    print(count_evens(n)) 
    print()
    # q2
    print(list_to_string(n))
    print()
    # q3
    print(lists_are_the_same(n,m))
    print(lists_are_the_same(n,p))
    print(lists_are_the_same(n,o))
    print()
    # q4
    print(list1_start_with_list2(p,n))
    print(list1_start_with_list2(n,p))
    print(list1_start_with_list2(n,m))
    print()
    #q5
    print(match_pattern(n,m))
    print(match_pattern(o,p))
    print(match_pattern(q,p))
    print()
    #q6
    print(duplicates(n))
    print(duplicates(m))
    print()
    #q7
    print(inst_velo(x, 0.3))
    print(inst_velo(x, 0.1))
    print(inst_velo(x, 0.2))
    print(inst_velo(x, 1))
    for i in range(len(x)):
        x[i] = round(0.1*random.randint(0,100),1)
    print(x)
    print(inst_velo(x, 0.3))
    print(inst_velo(x, 0.1))
    print(inst_velo(x, 0.2))
    print(inst_velo(x, 1))

    #q5 again
    list1 = [1,1,2,3,4]
    list2 = [1,2,3]
    print(match_pattern(list1,list2))
    

