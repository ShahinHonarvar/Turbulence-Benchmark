
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[:3]
    return sum(x for x in sub_list if x % -2 == 0 or x % 3 == 0)
