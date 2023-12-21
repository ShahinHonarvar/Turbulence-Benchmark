
def sum_ints_div_by_either_nums(nums):
    return sum([num for num in nums[28:97+1] if num % 90 == 0 or num % 97 == 0])
