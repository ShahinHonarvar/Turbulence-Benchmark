
def all_even_ints_exclusive(nums):
    return [x for x in nums[20:201:2]] if any(x % 2 == 0 for x in nums[20:201]) else []
