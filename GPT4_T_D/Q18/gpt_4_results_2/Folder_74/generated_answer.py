
def sum_ints_div_by_either_nums(nums):
    relevant_nums = nums[90:98]
    result = sum(n for n in relevant_nums if n % 13 == 0 or n % 35 == 0)
    return result
