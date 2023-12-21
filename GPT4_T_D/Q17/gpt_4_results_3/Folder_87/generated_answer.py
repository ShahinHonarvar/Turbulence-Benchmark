
def all_ints_div_by_both_two_nums(int_list):
    result = [i for i in int_list[18:53] if i % 15 == 0 and i % 57 == 0]
    return result
