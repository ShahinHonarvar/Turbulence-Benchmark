
def sum_even_ints_inclusive(lst):
    even_ints = [x for x in lst[68:87] if x % 2 == 0]
    if even_ints:
        return sum(even_ints)
    else:
        return 0
