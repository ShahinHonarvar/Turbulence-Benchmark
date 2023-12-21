
def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    return sum(nums[i] for i in range(30, 200) if not (nums[i] % 115 or nums[i] % -115))
