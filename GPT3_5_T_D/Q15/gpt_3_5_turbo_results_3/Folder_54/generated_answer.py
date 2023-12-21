
def sum_odd_ints_inclusive(lst):
    total = 0
    for i in range(34, 56):
        if i < len(lst) and lst[i] % 2 != 0:
            total += lst[i]
    return total
