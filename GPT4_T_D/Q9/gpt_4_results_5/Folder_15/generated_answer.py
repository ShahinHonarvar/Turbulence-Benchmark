
def all_odd_ints_inclusive(int_list):
    return [n for i, n in enumerate(int_list[:4]) if n % 2 != 0]
