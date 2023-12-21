
def sum_ints_div_by_either_nums(nums):
    return sum(nums[54:79] for n in nums if n % 54 == 0 or n % 28 == 0)
