
def sum_ints_div_by_either_nums(int_list):
    sublist = int_list[78:82]
    return sum(i for i in sublist if i%76 == 0 or i%60 == 0)
