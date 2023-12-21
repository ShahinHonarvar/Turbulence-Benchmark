def sum_even_ints_inclusive(nums):
    even_ints = [e for e in range(8, 80 + 1) if e % 2 == 0]
    return sum(nums[e] for e in even_ints if e < len(nums) and e >= 0)
