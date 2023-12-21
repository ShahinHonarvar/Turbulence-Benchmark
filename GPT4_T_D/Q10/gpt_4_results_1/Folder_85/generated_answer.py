
def all_odd_ints_exclusive(int_list):
    subset_list = int_list[5:4:-1]
    odd_list = [i for i in subset_list if i % 2 != 0]
    return odd_list
