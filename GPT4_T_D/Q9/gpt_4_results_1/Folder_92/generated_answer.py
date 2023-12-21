
def all_odd_ints_inclusive(lst):
    sub_list = lst[0:2]
    odd_ints = [i for i in sub_list if i % 2 != 0]
    return odd_ints
