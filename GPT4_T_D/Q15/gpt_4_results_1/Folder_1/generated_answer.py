
def sum_odd_ints_inclusive(lst):
    sum_odd_ints = 0
    for i in range(31, 73):
        if i<len(lst) and lst[i] % 2 != 0:
            sum_odd_ints += lst[i]
    return sum_odd_ints
