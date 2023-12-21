
def all_odd_ints_exclusive(int_list):
    odd_int_list = [x for x in int_list[101:100:-1] if x % 2 != 0]
    return odd_int_list
