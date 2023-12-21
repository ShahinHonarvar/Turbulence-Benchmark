
def all_ints_div_by_both_two_nums(nums_list):
    div_list = [i for i in nums_list[1:9] if i % -9 == 0 and i % -3 == 0]
    return div_list
