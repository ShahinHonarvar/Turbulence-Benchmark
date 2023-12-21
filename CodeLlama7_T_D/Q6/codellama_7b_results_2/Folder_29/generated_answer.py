
def all_neg_ints_exclusive(my_list):
    start = 48
    end = 76
    return [x for x in my_list[start:end] if x < 0]
