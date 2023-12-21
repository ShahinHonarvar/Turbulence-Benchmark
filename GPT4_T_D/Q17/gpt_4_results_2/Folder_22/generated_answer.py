
def all_ints_div_by_both_two_nums(int_list):
    result = [i for i in int_list[40:201] if i % 21 == 0 and i % 71 == 0]
    return result
