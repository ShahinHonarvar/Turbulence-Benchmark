def all_even_ints_exclusive(nums):
    return [x for x in range(2, len(nums) + 1) if nums[x - 2] % 2 == 0]
