
def sum_ints_div_by_either_nums(int_list):
    nums = int_list[90:98]
    sum_nums = sum([i for i in nums if i % 13 == 0 or i % 35 == 0])
    return sum_nums
