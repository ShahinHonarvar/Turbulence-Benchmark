
def sum_even_ints_inclusive(lst):
    sum_even = sum(i for i in lst[74:96] if i % 2 == 0)
    return sum_even if sum_even else 0
