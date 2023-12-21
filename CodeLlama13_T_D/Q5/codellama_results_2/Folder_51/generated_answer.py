
def all_neg_ints_inclusive(my_list):
    return [i for i in my_list if i < 0 and 1 <= abs(i) <= 8]
