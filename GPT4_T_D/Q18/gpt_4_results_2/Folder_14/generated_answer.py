
def sum_ints_div_by_either_nums(nums):
    div_nums = [num for num in nums[7:10] if num % 2 == 0 or num % 3 == 0]
    return sum(div_nums) if div_nums else 0
