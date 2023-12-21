def all_even_ints_exclusive(nums):
    evens = [n for n in range(59, 93) if n % 2 == 0]
    return [nums[i] for i in evens if nums[i] % 2 == 0]
