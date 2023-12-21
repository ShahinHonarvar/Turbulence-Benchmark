
def sum_odd_ints_inclusive(int_list):
    return sum(n for i, n in enumerate(int_list[:8]) if n % 2 != 0)
