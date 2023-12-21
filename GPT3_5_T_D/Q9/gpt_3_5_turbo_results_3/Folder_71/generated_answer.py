
def all_odd_ints_inclusive(lst):
    odd_ints = [n for n in lst[26:53] if n % 2 != 0]
    return odd_ints if odd_ints else []
