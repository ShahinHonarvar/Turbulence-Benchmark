
def sum_odd_ints_inclusive(list_int):
    sum_odd = 0
    for i in range(30, 88):
        if i < len(list_int) and list_int[i] % 2 != 0:
            sum_odd += list_int[i]
    return sum_odd
