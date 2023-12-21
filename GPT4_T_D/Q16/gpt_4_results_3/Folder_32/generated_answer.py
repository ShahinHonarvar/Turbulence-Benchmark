
def sum_even_ints_inclusive(num_list):
    return sum(n for i, n in enumerate(num_list[21:98]) if n % 2 == 0)
