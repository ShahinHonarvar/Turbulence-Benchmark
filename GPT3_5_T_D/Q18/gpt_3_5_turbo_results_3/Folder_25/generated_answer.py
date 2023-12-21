
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[25:81] if num % -20 == 0 or num % -26 == 0) if 25 <= len(nums) <= 80 else 0
