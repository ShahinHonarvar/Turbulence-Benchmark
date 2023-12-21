
def all_ints_div_by_both_two_nums(int_list):
    result = [i for i in int_list[61:89] if i % 31 == 0 and i % 11 == 0]
    return result
