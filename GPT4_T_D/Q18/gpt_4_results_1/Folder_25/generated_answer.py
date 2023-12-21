
def sum_ints_div_by_either_nums(nums):
    nums = nums[25:81]
    divisible_nums = [i for i in nums if i % -20 == 0 or i % -26 == 0]
    return sum(divisible_nums) if divisible_nums else 0
