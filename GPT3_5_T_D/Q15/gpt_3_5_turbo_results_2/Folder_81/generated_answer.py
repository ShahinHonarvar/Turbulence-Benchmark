
def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(10, 101):
        if i % 2 != 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum
