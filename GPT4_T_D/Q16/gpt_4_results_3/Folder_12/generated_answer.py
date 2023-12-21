
def sum_even_ints_inclusive(lst):
    return sum(n for i, n in enumerate(lst[14:65]) if n % 2 == 0)
