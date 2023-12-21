
def sum_even_ints_inclusive(lst):
    lst_subset = lst[29:80]
    sum_even = sum(i for i in lst_subset if i % 2 == 0)
    return sum_even
