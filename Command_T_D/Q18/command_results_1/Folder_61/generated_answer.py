
def sum_ints_div_by_either_nums(int_list):
    int_list = list(range(len(int_list)))
    return sum(int_list[i] for i in range(len(int_list)) if (int_list[i] % -5 == 0 or int_list[i] % -6 == 0))
