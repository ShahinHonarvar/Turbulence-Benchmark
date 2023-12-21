
def all_ints_div_by_both_two_nums(int_list):
    result = [i for i in int_list[25:81] if i % -20 == 0 and i % -26 == 0]
    return result
