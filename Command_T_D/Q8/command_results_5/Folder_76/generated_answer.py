def all_even_ints_exclusive(nums):
    return [n for n in range(361, 643, 2) if nums[n] % 2 == 0]
