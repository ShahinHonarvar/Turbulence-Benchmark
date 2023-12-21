def all_odd_ints_exclusive(nums):
    return [n for n in range(100, 101) if n % 2 == 1 and n in nums]
