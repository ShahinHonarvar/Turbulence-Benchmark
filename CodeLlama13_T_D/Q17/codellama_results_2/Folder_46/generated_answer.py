
def all_ints_div_by_both_two_nums(list_of_integers):
    return list(filter(lambda x: x % 55 == 0 and x % 36 == 0, list_of_integers[11:47]))
