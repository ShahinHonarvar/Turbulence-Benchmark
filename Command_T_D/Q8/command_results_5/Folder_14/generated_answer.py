def all_even_ints_exclusive(nums):
    even_ints = [e for e in range(1, len(nums) + 1) if nums[e - 1] % 2 == 0]
    return [nums[e - 1] for e in even_ints if e > 0 and e < len(nums) + 1]
