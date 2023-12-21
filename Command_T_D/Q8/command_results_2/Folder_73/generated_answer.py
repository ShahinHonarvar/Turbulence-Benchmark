def all_even_ints_exclusive(nums):
    even = [i for i in range(36, 85, 2) if all(nums[i] % 2 == e for e in range(2, 8)) and i not in nums]
    return even
