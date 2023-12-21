
def sum_ints_div_by_either_nums(nums):
    return sum([n for n in nums[3:9+1] if n % 6 == 0 or n % 1 == 0])
