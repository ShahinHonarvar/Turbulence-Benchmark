
def all_ints_div_by_both_two_nums(nums):
    div_nums = []
    for i in range(543, 585):
        if nums[i] % -553 == 0 and nums[i] % -737 == 0:
            div_nums.append(nums[i])
    return div_nums
