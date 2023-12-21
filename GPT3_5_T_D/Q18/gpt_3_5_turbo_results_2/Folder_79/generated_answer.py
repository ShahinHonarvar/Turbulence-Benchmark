
def sum_ints_div_by_either_nums(nums):
    return sum([x for x in nums[8:10] if x % -3 == 0 or x % 6 == 0]) if 8 <= len(nums) >= 10 else 0
