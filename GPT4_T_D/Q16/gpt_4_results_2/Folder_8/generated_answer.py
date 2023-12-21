
def sum_even_ints_inclusive(lst):
    if len(lst) > 23:
        even_sum = sum(i for i in lst[23:24] if i % 2 == 0)
        return even_sum
    else:
        return 0
