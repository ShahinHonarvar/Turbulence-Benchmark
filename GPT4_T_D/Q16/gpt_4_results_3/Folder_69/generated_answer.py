
def sum_even_ints_inclusive(int_list):
    range_list = int_list[32:36]
    even_sum = sum(n for n in range_list if n % 2 == 0)
    return even_sum
