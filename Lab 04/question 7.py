def check_leap(y):
    return y%4 == 0 and (y%100 != 0 or y%400 == 0)

# part a
def next_day(y, m, d):
    year = y
    month = m
    day = d+1
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap(y):
        month_lengths[1] = 29
    while day >= month_lengths[((month-1)%12)]:
        day -= month_lengths[(month-1)%12]-1
        month += 1
        if month > 12:
            while month > 12:
                month -= 12
                year += 1
    return year,month,day

# part b
def all_days(y1, m1, d1, y2, m2 ,d2):
    y, m, d, yy, mm, dd, num_days = 0,0,0,0,0,0,0
    if (y1<y2) or (y1==y2 and m1<m2) or (y1==y2 and m1==m2 and d1 < d2):
        y, yy = y1, y2
        m, mm = m1, m2
        d, dd = d1, d2
    if y1==y2 and m1==m2 and d1==d2:
        return 0
    else:
        y, yy = y2, y1
        m, mm = m2, m1
        d, dd = d2, d1
    y,m,d = next_day(y,m,d)
    num_days +=1
    while (y<yy) or (y==yy and m<mm) or (y==yy and m==mm and d < dd):
        print(f'{y}/{m}/{d}')
        y,m,d = next_day(y,m,d)
        num_days +=1
    return num_days


if __name__ == '__main__':
    print(next_day(int(input('year: ')), int(input('month: ')), int(input('day: '))))
    print(all_days(int(input('year 1: ')), int(input('month 1: ')), int(input('day 1: ')), int(input('year 2: ')), int(input('month 2: ')), int(input('day 2: '))))
