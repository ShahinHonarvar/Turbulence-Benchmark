
def sum_even_ints_inclusive(lst):
    even_ints_in_range = [elem for i, elem in enumerate(lst) if 66 <= i <= 93 and elem % 2 == 0]
    if even_ints_in_range:
        return sum(even_ints_in_range)
    else:
        return 0
