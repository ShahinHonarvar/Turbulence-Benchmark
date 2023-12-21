
def all_neg_ints_exclusive(my_list):
    return [x for x in my_list if x < 0 and 86 <= len(my_list) - my_list.index(x) <= 99]
