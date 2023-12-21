
def sum_ints_div_by_either_nums(int_list):
    result = sum(i for i in int_list[7:10] if i % -9 == 0 or i % -7 == 0)
    return result
