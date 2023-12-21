
def all_odd_ints_exclusive(int_list):
    odd_ints = [x for i, x in enumerate(int_list[1:7]) if x % 2 != 0]
    return odd_ints
