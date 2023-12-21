
def sum_even_ints_inclusive(lst):
    if len(lst) > 29:
        even_sum = sum(i for i in lst[29:30] if i % 2 == 0)
        return even_sum
    else:
        return 0
