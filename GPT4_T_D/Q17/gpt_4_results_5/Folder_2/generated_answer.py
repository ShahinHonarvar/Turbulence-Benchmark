
def all_ints_div_by_both_two_nums(nums_list):
    div_by_both_nums = []
    for i in range(73, 87):
        if nums_list[i] % 54 == 0 and nums_list[i] % 82 == 0:
            div_by_both_nums.append(nums_list[i])
    return div_by_both_nums
