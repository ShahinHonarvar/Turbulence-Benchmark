
def all_odd_ints_exclusive(int_list):
    sublist = int_list[63:96]
    odd_list = list(filter(lambda x: (x % 2 != 0), sublist))
    return odd_list
