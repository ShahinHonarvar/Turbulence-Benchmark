
def all_ints_div_by_both_two_nums(int_list):
    divisible = [i for i in int_list[38:82] if i % -61 == 0 and i % -71 == 0]
    return divisible
