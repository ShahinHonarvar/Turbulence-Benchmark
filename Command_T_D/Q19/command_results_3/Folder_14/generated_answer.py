def all_ints_not_div_by_num(list_of_ints):
    list_of_ints = [i for i in list_of_ints if not i%8]
    return [i for i in list_of_ints if i > 1 and i < 7]
