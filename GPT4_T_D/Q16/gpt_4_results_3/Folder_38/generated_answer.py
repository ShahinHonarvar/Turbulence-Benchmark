
def sum_even_ints_inclusive(int_list):
    sum_even = sum(n for i, n in enumerate(int_list[22:64]) if n % 2 == 0)
    return sum_even
