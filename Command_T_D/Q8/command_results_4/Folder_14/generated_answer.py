def all_even_ints_exclusive(nums):
    return [i for i in range(2, 8) if i in nums and nums[i] % 2 == 0]
