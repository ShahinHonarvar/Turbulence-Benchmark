
def sum_even_ints_inclusive(int_list):
    even_sum = sum(n for i, n in enumerate(int_list[:7]) if n % 2 == 0)
    return even_sum
