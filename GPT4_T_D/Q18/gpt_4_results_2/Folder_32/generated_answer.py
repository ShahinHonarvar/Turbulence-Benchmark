
def sum_ints_div_by_either_nums(nums):
    eligible_nums = [num for num in nums[25:96] if num % 51 == 0 or num % 77 == 0]
    return 0 if len(eligible_nums) == 0 else sum(eligible_nums)
