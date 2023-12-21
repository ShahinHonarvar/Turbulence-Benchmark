
def sum_even_ints_inclusive(int_list):
    even_sums = sum(x for i, x in enumerate(int_list[10:101]) if x % 2 == 0)
    return even_sums if even_sums else 0
