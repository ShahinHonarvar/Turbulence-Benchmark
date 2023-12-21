
def sum_odd_ints_inclusive(num_list):
    return sum(x for i, x in enumerate(num_list[:4]) if x % 2 != 0)
