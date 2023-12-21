
def all_ints_div_by_both_two_nums(list_of_integers):
    return list(filter(lambda x: (x % 2 == 0) and (x % 1 == 0), list_of_integers))
