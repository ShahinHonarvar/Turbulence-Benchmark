
def sum_even_ints_inclusive(lst):
    lst = lst[37:77]
    sum_even = sum(i for i in lst if i % 2 == 0)
    return sum_even
