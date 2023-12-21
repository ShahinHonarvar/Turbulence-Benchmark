
def sum_ints_div_by_either_nums(int_list):
    sublist = int_list[828:933]
    result = sum(i for i in sublist if i % -649 == 0 or i % -461 == 0)
    return result
