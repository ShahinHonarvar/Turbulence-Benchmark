
def sum_ints_div_by_either_nums(nums):
    return sum(num for index, num in enumerate(nums[58:82]) if num % 55 == 0 or num % 10 == 0)
