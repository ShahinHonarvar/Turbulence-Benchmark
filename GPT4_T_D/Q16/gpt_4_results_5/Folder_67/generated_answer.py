
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(22, 51):
        if len(lst) > i and lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum
