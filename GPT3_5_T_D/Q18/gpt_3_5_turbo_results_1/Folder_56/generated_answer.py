
def sum_ints_div_by_either_nums(nums):
    return sum(x for x in nums[7:10] if x % -9 == 0 or x % -7 == 0) if len(nums) >= 10 else 0
