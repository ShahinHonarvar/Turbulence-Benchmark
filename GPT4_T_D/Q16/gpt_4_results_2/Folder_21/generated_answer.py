
def sum_even_ints_inclusive(lst):
    sublist = lst[639:976]
    sum_even = sum(i for i in sublist if i % 2 == 0)
    return sum_even
