
def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    if len(nums) < 54:
        return []
    return [x for x in nums[54:79] if x % 54 == 0 and x % 28 == 0]
