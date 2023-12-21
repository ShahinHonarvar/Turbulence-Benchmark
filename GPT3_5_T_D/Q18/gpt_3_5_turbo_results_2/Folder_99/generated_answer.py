
def sum_ints_div_by_either_nums(nums):
    return sum(num for num in nums[154:799] if num % 275 == 0 or num % 580 == 0) if 154 <= len(nums) <= 798 else 0
