
def all_ints_div_by_both_two_nums(nums):
    return [nums[i] for i in range(90, 201) if nums[i] % 13 == nums[i] % 31 == 0]
