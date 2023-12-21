
def sum_even_ints_inclusive(lst):
    lst = lst[29:94]
    return sum(i for i in lst if i % 2 == 0)
