
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[10:29] if x % -61 == 0 or x % -64 == 0) if 10 <= len(nums) else 0
