
def sum_ints_div_by_either_nums(int_list):
    return sum(el for el in int_list[6:10] if el % -1 == 0 or el % -10 == 0)
