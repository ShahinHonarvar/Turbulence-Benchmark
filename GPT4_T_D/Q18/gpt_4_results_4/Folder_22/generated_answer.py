
def sum_ints_div_by_either_nums(int_list):
    valid_range = int_list[40:201]
    sum_valid_nums = sum(i for i in valid_range if i % 21 == 0 or i % 71 == 0)
    return sum_valid_nums
