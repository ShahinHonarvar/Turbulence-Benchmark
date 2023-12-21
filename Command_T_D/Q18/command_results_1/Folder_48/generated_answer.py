
def sum_ints_div_by_either_nums(nums):
    start, stop, step = 306, 957, 1
    return sum(nums[start:stop:step] if num % 982 == 0 or num % 319 == 0 else [] for num in nums)
