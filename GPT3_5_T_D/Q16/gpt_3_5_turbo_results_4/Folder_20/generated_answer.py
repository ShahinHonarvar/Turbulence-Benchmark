
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(56, 67):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_even += lst[i]
    return sum_even
