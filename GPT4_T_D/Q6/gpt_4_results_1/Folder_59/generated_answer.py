
def all_neg_ints_exclusive(my_list):
    sublist = my_list[1:9]
    result = [i for i in sublist if i < 0]
    return result
