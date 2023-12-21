
def all_neg_ints_exclusive(my_list):
    return [x for x in my_list if x < 0 and 38 <= len(my_list) - 1 - my_list.index(x) <= 52]
