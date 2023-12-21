
def all_odd_ints_exclusive(int_list):
    odd_ints = [x for i, x in enumerate(int_list) if i > 29 and i < 53 and x % 2 != 0]
    return odd_ints
