
def sum_even_ints_inclusive(lst):
    sum_evens = 0
    for i in range(68, 87):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_evens += lst[i]
    return sum_evens
