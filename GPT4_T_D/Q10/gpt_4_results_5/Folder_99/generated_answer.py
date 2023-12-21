
def all_odd_ints_exclusive(integer_list):
    sublist = integer_list[296:573]
    odd_ints = [i for i in sublist if i % 2 != 0]
    return odd_ints
