
def sum_ints_div_by_either_nums(nums):
    return sum(num for i, num in enumerate(nums[29:46]) if num % 27 == 0 or num % 81 == 0)
