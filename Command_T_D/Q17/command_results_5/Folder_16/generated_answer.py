
def all_ints_div_by_both_two_nums(nums):
    if 55 <= len(nums) <= 80:
        return [x for x in nums[55:-2] if x % 22 == 0 and x % 32 == 0]
    return []
