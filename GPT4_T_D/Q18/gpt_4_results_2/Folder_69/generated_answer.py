
def sum_ints_div_by_either_nums(int_list):
    nums_in_range = int_list[61:89]
    return sum(i for i in nums_in_range if i % 31 == 0 or i % 11 == 0)
