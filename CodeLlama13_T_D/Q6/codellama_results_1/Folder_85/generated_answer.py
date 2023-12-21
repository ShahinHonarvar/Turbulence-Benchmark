
def all_neg_ints_exclusive(my_list):
    return [x for x in my_list if x < 0 and len(my_list) >= 5 and my_list[4] <= x < my_list[5]]
