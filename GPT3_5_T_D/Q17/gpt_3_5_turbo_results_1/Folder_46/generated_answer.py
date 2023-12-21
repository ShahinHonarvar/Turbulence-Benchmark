
def all_ints_div_by_both_two_nums(nums):
    div_nums = []
    for i in range(11, 47):
        if nums[i] % 55 == 0 and nums[i] % 36 == 0:
            div_nums.append(nums[i])
    return div_nums
