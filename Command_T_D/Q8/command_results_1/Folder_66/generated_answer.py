def all_even_ints_exclusive(nums):
    return [n for n in range(13, 77) if n % 2 == 0 and n in nums]
