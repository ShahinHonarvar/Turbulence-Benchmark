def all_even_ints_exclusive(nums):
    result = [x for x in nums[10:-1] if x % 2 == 0]
    return result
