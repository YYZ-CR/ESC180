def check_leap(y):
    return y%4 == 0 and (y%100 != 0 or y%400 == 0)

# part a
def next_day(y, m, d):
    year = y
    month = m
    day = d
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_leap(y):
        month_lengths[1] = 29
    while day >= month_lengths[((month-1)%12)]:
        month += 1
        day -= month_lengths[(month-1)%12]-1
        if month > 12:
            while month > 12:
                month -= 12
                year += 1
        else:
            month = m
            day += 1
    print(f'{year}/{month}/{day}')

if __name__ == '__main__':
    next_day(int(input('year: ')), int(input('month: ')), int(input('day: ')))
    