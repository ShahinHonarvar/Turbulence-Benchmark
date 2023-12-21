
def sum_odd_ints_inclusive(lst):
    sum_ints = 0
    for i in range(14, 65):
        if i < len(lst) and lst[i] % 2 != 0:
            sum_ints += lst[i]
    return sum_ints
